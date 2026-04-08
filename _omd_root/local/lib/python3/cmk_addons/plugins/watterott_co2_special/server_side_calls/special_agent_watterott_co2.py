#!/usr/bin/env python3
# Shebang needed only for editors

from cmk.server_side_calls.v1 import noop_parser, SpecialAgentConfig, SpecialAgentCommand, HostConfig
import json

# {"outer": ["filesystem", {"file": "/tmp/$HOSTNAME$.txt", "maxage": 180.0}]}
# {"outer": ["network", {"host": "$HOSTNAME$"}]}
# The most common ones are $HOSTNAME$, $HOSTALIAS$ or $HOSTADDRESS$.

def command_function(params, host_config):
    args = []
    if "filesystem" in params["outer"]:
        args.append("--file")
        args.append(params["outer"][1]["file"].replace("$HOSTNAME$", host_config.name).replace("$HOSTADDRESS$", host_config.ipv4_config.address).replace("$HOSTALIAS$", host_config.alias))
        args.append("--maxage")
        args.append(str(params["outer"][1]["maxage"]))
    else:
        args.append("--host")
        args.append(params["outer"][1]["host"].replace("$HOSTNAME$", host_config.name).replace("$HOSTADDRESS$", host_config.ipv4_config.address).replace("$HOSTALIAS$", host_config.alias))
    yield SpecialAgentCommand(command_arguments=args)

special_agent_ometemp = SpecialAgentConfig(
    name="watterott_co2_special",
    parameter_parser=noop_parser,
    commands_function=command_function
)
