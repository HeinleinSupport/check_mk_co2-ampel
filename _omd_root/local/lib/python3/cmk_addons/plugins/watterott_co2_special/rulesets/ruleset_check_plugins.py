#!/usr/bin/env python3

from cmk.rulesets.v1 import Title, Help
from cmk.rulesets.v1.form_specs import DefaultValue, DictElement, Dictionary, Integer, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import CheckParameters, HostCondition, Topic

def parameter_form_watterott_co2_co2():
    return Dictionary(
        elements = {
            "upper": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("CO₂ concentration thresholds"),
                    form_spec_template = Integer(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(800, 1200)),
                ),
                required = True,
            ),
            "hysteresis": DictElement(
                parameter_form = Integer(
                    title = Title("Hysteresis for high-low pass"),
                    help_text = Help("In this version of the check plug-in the hysteresis is ignored."),
                    unit_symbol = "ppm",
                    prefill = DefaultValue(100),
                ),
                required = True,
            ),
        }
    )

rule_spec_watterott_co2_special_co2 = CheckParameters(
    name = "watterott_co2_special_co2",
    title = Title("CO₂ concentration levels for Watterott CO₂ sensor"),
    topic = Topic.ENVIRONMENTAL,
    parameter_form = parameter_form_watterott_co2_co2,
    condition = HostCondition(),
)
