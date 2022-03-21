#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Adrien Wehrlé, University of Zurich, Switzerland
"""

import json
import glob

def test_file_opening():
    sat_files = sorted(glob.glob('./satellites/*.json'))

    for file in sat_files:
            with open(file) as json_file:
                data = json.load(json_file)
