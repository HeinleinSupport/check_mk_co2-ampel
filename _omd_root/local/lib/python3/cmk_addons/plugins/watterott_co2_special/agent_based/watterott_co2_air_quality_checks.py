#!/usr/bin/env python3

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels
import itertools
import json

def parse_watterott_co2_special(string_table):
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))
    return parsed
    
def discover_watterott_co2_co2(section):
    yield Service()
    
def check_watterott_co2_co2(params, section):
    if section["c"] > 1400.0:
        yield Result(
            state=State(State.CRIT),
            summary="You are dead soon!",
        )
    elif section["c"] > 800.0:
         yield Result(
            state=State(State.WARN),
            summary="Ventilate if you do not want to be dead soon.",
        )
    else:
         yield Result(
            state=State(State.OK),
            summary="Everything is fine.",
        )
    yield Metric(
        name = "parts_per_million",
        value = section["c"],
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
    return
    if section["t"] > 24.0:
        yield Result(
            state=State(State.CRIT),
            summary="You are grilled soon!",
        )
    elif section["t"] > 22.0:
         yield Result(
            state=State(State.WARN),
            summary="Shade if you do not want to be grilled soon.",
        )
    else:
         yield Result(
            state=State(State.OK),
            summary="Everything is fine.",
        )
    yield Metric(
        name = "temp",
        value = section["t"],
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
    check_default_parameters = {},
    #check_default_parameters = { 
    #    "stateregular": int(State.WARN), 
    #    "statesecurity": int(State.CRIT), 
    #    "statereboot": int(State.CRIT) 
    #},
    #check_ruleset_name = "watterott_co2_special_co2",
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

