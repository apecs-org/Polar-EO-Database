#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Adrien Wehrlé, University of Zurich, Switzerland
"""

import json
import glob


class tests:
    def __init__(self) -> None:

        self.json_entries = [
            "Ecology",
            "Regions covered",
            "Oceanography",
            "The Arctic",
            "Signal/sensor/ instrument type",
            "Processing software",
            "The Himalayas",
            "Period covered (end)",
            "Period covered (start)",
            "Other regions",
            "Climate Science",
            "Other fields",
            "Sensor name (if level 1)",
            "Scientific application",
            "Geology",
            "Validation",
            "RS dataset name",
            "Antarctica",
            "Is open data?",
            "Dataset level",
            "Sea Ice",
            "Data access platform",
            "Satellite name (if level 1)",
            "Parameters sought",
            "Glaciology",
            "Hydrology",
        ]

        return None

    def test_json_opening() -> None:
        
        sat_files = sorted(glob.glob("./data/*.json"))

        for file in sat_files:
            with open(file) as json_file:
                data = json.load(json_file)
                assert isinstance(data, dict)

        return None

    def test_json_entries():

        return None
