#!/usr/bin/env python3

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, check_levels
import itertools
import json

def parse_watterott_co2_special(string_table):
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))
    return parsed
    
def discover_watterott_co2_co2(section):
    yield Service()
    
def check_watterott_co2_co2(params, section):
    yield from check_levels(
        section["c"],
        levels_upper=params["upper"],
        metric_name="parts_per_million",
        label="CO₂ sensor value",
        render_func=lambda v: "%d ppm" % v,
    )

def discover_watterott_co2_temp(section):
    yield Service()

def check_watterott_co2_temp(params, section):
    yield from check_levels(
        section["t"],
        levels_upper=params["upper"],
        levels_lower=params["lower"],
        metric_name="temp",
        label="Temperature sensor value",
        render_func=lambda v: "%.1f°C" % v,
    )

def discover_watterott_co2_humidity(section):
    yield Service()
    
def check_watterott_co2_humidity(params, section):
    yield from check_levels(
        section["h"],
        levels_upper=params["upper"],
        levels_lower=params["lower"],
        metric_name="humidity",
        label="Humidity sensor value",
        render_func=lambda v: "%.1f%%" % v,
    )

agent_section_watterott_co2_special = AgentSection(
    name = "watterott_co2_special",
    parse_function = parse_watterott_co2_special,
)

check_plugin_watterott_co2_co2 = CheckPlugin(
    name = "watterott_co2_special_co2",
    sections = [ "watterott_co2_special" ],
    service_name = "CO₂ concentration Watterott sensor",
    discovery_function = discover_watterott_co2_co2,
    check_function = check_watterott_co2_co2,
    check_default_parameters = {
        "upper": ("fixed", (800, 1200)),
        "hysteresis": 100,
    },
    check_ruleset_name = "watterott_co2_special_co2",
)

check_plugin_watterott_co2_temp = CheckPlugin(
    name = "watterott_co2_special_temp",
    sections = [ "watterott_co2_special" ],
    service_name = "Temperature Watterott sensor",
    discovery_function = discover_watterott_co2_temp,
    check_function = check_watterott_co2_temp,
    check_default_parameters = {
        "upper": ("no_levels", None),
        "lower": ("no_levels", None),
    },
    check_ruleset_name = "watterott_co2_special_temp",
)

check_plugin_watterott_co2_humidity = CheckPlugin(
    name = "watterott_co2_special_humidity",
    sections = [ "watterott_co2_special" ],
    service_name = "Humidity Watterott sensor",
    discovery_function = discover_watterott_co2_humidity,
    check_function = check_watterott_co2_humidity,
    check_default_parameters = {
        "upper": ("no_levels", None),
        "lower": ("no_levels", None),
    },
    check_ruleset_name = "watterott_co2_special_humidity",
)
