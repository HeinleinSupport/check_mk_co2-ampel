#!/usr/bin/env python3
# Shebang needed only for editors

from cmk.server_side_calls.v1 import noop_parser, SpecialAgentConfig, SpecialAgentCommand, HostConfig, replace_macros

# {"outer": ["filesystem", {"file": "/tmp/$HOSTNAME$.txt", "maxage": 180.0}]}
# {"outer": ["network", {"host": "$HOSTNAME$"}]}
# The most common ones are $HOSTNAME$, $HOSTALIAS$ or $HOSTADDRESS$.

def command_function(params, host_config: HostConfig):
    args = []
    if "filesystem" in params["outer"]:
        args.append("--file")
        args.append(replace_macros(params["outer"][1]["file"], host_config.macros))
        args.append("--maxage")
        args.append(str(params["outer"][1]["maxage"]))
    else:
        args.append("--host")
        args.append(replace_macros(params["outer"][1]["host"], host_config.macros))
    yield SpecialAgentCommand(command_arguments=args)

special_agent_ometemp = SpecialAgentConfig(
    name="watterott_co2_special",
    parameter_parser=noop_parser,
    commands_function=command_function
)
