#!/usr/bin/env python3
# Shebang needed only for editors

from cmk.rulesets.v1.form_specs import Dictionary, DictElement, Float, String, TimeSpan, TimeMagnitude, CascadingSingleChoice, CascadingSingleChoiceElement, DefaultValue
from cmk.rulesets.v1.rule_specs import SpecialAgent, Topic, Help, Title

def _formspec():
    return Dictionary(
        title=Title("Watterot CO2 sensor (special agent)"),
        help_text=Help("Configure the special agent to either read from a file or contact the HTTP server on the sensor board."),
        elements={
            "outer": DictElement(
                required=True,
                parameter_form=CascadingSingleChoice(
                    title=Title("Connection method"),
                    prefill=DefaultValue("network"),
                    elements=[
                        CascadingSingleChoiceElement(
                            name="network",
                            title=Title("Connect via HTTP"),
                            # help=Help("Specify host to connect to. Do not insert the full URL, only host name or IP address. The URL will be constructed from this."),
                            parameter_form=Dictionary(
                                title=Title("Host name or IP address"),
                                elements={
                                    "host": DictElement(
                                        required=True,
                                        parameter_form=String(
                                            title=Title("Host name or IP address"),
                                            prefill=DefaultValue("$HOSTADDRESS$"),
                                            macro_support=True,
                                        ),
                                    ),
                                },
                            ),
                        ),
                        CascadingSingleChoiceElement(
                            name="filesystem",
                            title=Title("Read from file system"),
                            parameter_form=Dictionary(
                                title=Title("Parameters for reading from file system"),
                                elements={
                                    "file": DictElement(
                                        required=True,
                                        parameter_form=String(
                                            title=Title("File to read"),
                                            # help=Help("This file must contain an exact dump of what's available on the /json/ endpoint of the Watterott CO2-Ampel."),
                                            macro_support=True,
                                        ),
                                    ),
                                    "maxage": DictElement(
                                        required=True,
                                        parameter_form=TimeSpan(
                                            title=Title("Ignore files older than (use 0 for no limit)"),
                                            displayed_magnitudes=[TimeMagnitude.SECOND, TimeMagnitude.MINUTE],
                                            prefill=DefaultValue(180.0),
                                        ),
                                    ),
                                },
                            ),
                        ),
                    ],
                ),
            ),
        }
    )

rule_spec_watterott_co2_special = SpecialAgent(
    topic=Topic.ENVIRONMENTAL,
    name="watterott_co2_special",
    title=Title("Watterott CO2 sensor (special agent)"),
    parameter_form=_formspec
)
