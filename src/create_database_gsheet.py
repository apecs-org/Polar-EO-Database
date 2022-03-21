#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

import glob
import json
import numpy as np
import gspread
import pandas as pd
import sys
import gspread_dataframe as gd

# setup API account
gc = gspread.service_account("./src/apecs-remote-sensing-database-e3d1516b4935.json")

# Open a sheet from a spreadsheet in one go
sheet = gc.open("APECS Remote Sensing Database - AW tests").sheet1

# clear entire work sheet
sheet.clear()

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

# insert all columns in first row
sheet.insert_row(list(gsheet_columns))

entries_list = []

for row, entry in enumerate(db_entries):

    # add nan to missing columns
    for column in gsheet_columns:
        entry.setdefault(column, np.nan)

    entries_list.append(list(entry.values()))

entries_df = pd.DataFrame(entries_list, columns=gsheet_columns)

# push entries to sheet
gd.set_with_dataframe(sheet, entries_df)
