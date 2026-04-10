#!/usr/bin/env python3

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, check_levels
from cmk.plugins.lib.temperature import check_temperature
from cmk.plugins.lib.humidity import check_humidity
import itertools
import json

def parse_watterott_co2_special(string_table):
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))
    return parsed
    
def discover_watterott_co2_co2(section):
    if "c" in section:
        yield Service()
    
def check_watterott_co2_co2(params, section):
    if "c" in section:
        yield from check_levels(
            section["c"],
            levels_upper=params["upper"],
            metric_name="parts_per_million",
            label="CO₂ sensor value",
            render_func=lambda v: "%d ppm" % v,
        )

def discover_watterott_co2_temp(section):
    if "t" in section:
        yield Service(item="Watterott sensor")

def check_watterott_co2_temp(item, params, section):
    if item == "Watterott sensor" and "t" in section:
        yield from check_temperature(
            reading=section["t"],
            params=params,
        )

def discover_watterott_co2_humidity(section):
    if "h" in section:
        yield Service(item="Watterott sensor")
    
def check_watterott_co2_humidity(item, params, section):
    if item == "Watterott sensor" and "h" in section:
        yield from check_humidity(
            humidity=section["h"],
            params=params,
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
    service_name = "Temperature %s",
    discovery_function = discover_watterott_co2_temp,
    check_function = check_watterott_co2_temp,
    check_default_parameters = {},
    check_ruleset_name = "temperature",
)

check_plugin_watterott_co2_humidity = CheckPlugin(
    name = "watterott_co2_special_humidity",
    sections = [ "watterott_co2_special" ],
    service_name = "Humidity %s",
    discovery_function = discover_watterott_co2_humidity,
    check_function = check_watterott_co2_humidity,
    check_default_parameters = {},
    check_ruleset_name = "humidity",
)
