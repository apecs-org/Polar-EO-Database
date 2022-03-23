#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Adrien Wehrlé, University of Zurich, Switzerland
"""

import json
import glob


class TestJSON:
    def test_json_opening(self) -> None:
        """
        Ensure JSON files integrity.
        """

        # list all JSON files
        self.sat_files = sorted(glob.glob("./data/*.json"))

        # store all JSON objects in a list to access data
        # without opening the files over and oer
        self.database_objects = []

        # test if every single file can be opened properly
        for file in self.sat_files:
            with open(file) as json_file:
                data = json.load(json_file)
                assert isinstance(data, dict)
                self.database_objects.append(data)

        return None

    def test_json_entries(self):
        """
        Verify JSON entries are part of the list of
        possible entries for the database.
        """

        # an example of all possible json entries
        possible_json_entries = [
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

        # test if all existing keys in JSON file are included
        # in the list of possible JSON entries
        for database_object in self.database_objects:

            assert all(key in possible_json_entries for key in database_object.keys())

        return None
