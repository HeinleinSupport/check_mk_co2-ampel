#!/usr/bin/env python3

from cmk.rulesets.v1 import Label, Title
from cmk.rulesets.v1.form_specs import Percentage, BooleanChoice, DefaultValue, DictElement, Dictionary, Float, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import CheckParameters, HostAndItemCondition, Topic

def parameter_form_watterott_co2_humidity():
    return Dictionary(
        elements = {
            "humidity_lower": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Lower relative humidity threshold"),
                    form_spec_template = Percentage(),
                    level_direction = LevelDirection.LOWER,
                    prefill_fixed_levels = DefaultValue(value=(30.0, 20.0)),
                ),
                required = True,
            ),
            "humidity_upper": DictElement(
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
            "humidity_lower": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Lower temperature threshold"),
                    form_spec_template = Float(),
                    level_direction = LevelDirection.LOWER,
                    prefill_fixed_levels = DefaultValue(value=(12.0, 10.0)),
                ),
                required = True,
            ),
            "humidity_upper": DictElement(
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

rule_spec_watterott_co2_special_humidity = CheckParameters(
    name = "watterott_co2_special_humidity",
    title = Title("Humidity levels for Watterott CO2 sensor"),
    topic = Topic.ENVIRONMENTAL,
    parameter_form = parameter_form_watterott_co2_humidity,
    condition = HostAndItemCondition(item_title=Title("Humidity Watterott sensor")),
)

rule_spec_watterott_co2_special_temp = CheckParameters(
    name = "watterott_co2_special_temp",
    title = Title("Temperature levels for Watterott CO2 sensor"),
    topic = Topic.ENVIRONMENTAL,
    parameter_form = parameter_form_watterott_co2_temperature,
    condition = HostAndItemCondition(item_title=Title("Temperature Watterott sensor")),
)
