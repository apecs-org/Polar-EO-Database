#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

import json
import glob

# list all database entries
json_files = glob.glob("./data/*.json")

for file in json_files:

    # open JSON file and store in dict
    data = json.load(open(file))

    # only keep non-nan values
    data_nonan = {k: v for k, v in data.items() if v == v}

    # push back modified dict
    open(file, "w").write(json.dumps(data_nonan, indent=4))
