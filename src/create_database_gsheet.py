#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

import glob
import json

# list all database entries
json_files = glob.glob("./data/*.json")

# store database entries so they are opened only once
db_entries = []

# prepare google sheet columns
gsheet_columns = set()

for file in json_files:

    # access and store entry objects
    with open(file) as f:
        db_entry = json.load(f)
    db_entries.append(db_entry)

    # update set if new object not listed yet
    gsheet_columns.update(list(db_entry.keys()))

print(gsheet_columns)
