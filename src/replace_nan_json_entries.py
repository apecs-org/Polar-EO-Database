#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

import json
import glob
import cmath

# list all database entries
json_files = glob.glob("./data/*.json")

for file in json_files:

    # open JSON file and store in dict
    with open(file, "r+") as f:
        data = json.load(f)

        # only keep non-nan values
        data_nonan = {k: v for k, v in data.items() if not cmath.isnan(v)}

        # push back modified dict
        json.dump(data_nonan, f, indent=4)
