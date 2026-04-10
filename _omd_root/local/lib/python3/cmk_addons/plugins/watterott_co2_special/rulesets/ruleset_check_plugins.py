#!/usr/bin/env python3

from cmk.rulesets.v1 import Label, Title, Help
from cmk.rulesets.v1.form_specs import Percentage, BooleanChoice, DefaultValue, DictElement, Dictionary, Float, Integer, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import CheckParameters, HostCondition, Topic

def parameter_form_watterott_co2_humidity():
    return Dictionary(
        elements = {
            "lower": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Lower relative humidity threshold"),
                    form_spec_template = Percentage(),
                    level_direction = LevelDirection.LOWER,
                    prefill_fixed_levels = DefaultValue(value=(30.0, 20.0)),
                ),
                required = True,
            ),
            "upper": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Upper relative humidity threshold"),
                    form_spec_template = Percentage(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(70.0, 80.0)),
                ),
                required = True,
            ),
        }
    )

def parameter_form_watterott_co2_temperature():
    return Dictionary(
        elements = {
            "lower": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Lower temperature threshold"),
                    form_spec_template = Float(),
                    level_direction = LevelDirection.LOWER,
                    prefill_fixed_levels = DefaultValue(value=(12.0, 10.0)),
                ),
                required = True,
            ),
            "upper": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Upper temperature threshold"),
                    form_spec_template = Float(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(24.0, 28.0)),
                ),
                required = True,
            ),
        }
    )

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

rule_spec_watterott_co2_special_humidity = CheckParameters(
    name = "watterott_co2_special_humidity",
    title = Title("Humidity levels for Watterott CO₂ sensor"),
    topic = Topic.ENVIRONMENTAL,
    parameter_form = parameter_form_watterott_co2_humidity,
    condition = HostCondition(),
)

rule_spec_watterott_co2_special_temp = CheckParameters(
    name = "watterott_co2_special_temp",
    title = Title("Temperature levels for Watterott CO₂ sensor"),
    topic = Topic.ENVIRONMENTAL,
    parameter_form = parameter_form_watterott_co2_temperature,
    condition = HostCondition(),
)

rule_spec_watterott_co2_special_co2 = CheckParameters(
    name = "watterott_co2_special_co2",
    title = Title("CO₂ concentration levels for Watterott CO₂ sensor"),
    topic = Topic.ENVIRONMENTAL,
    parameter_form = parameter_form_watterott_co2_co2,
    condition = HostCondition(),
)
