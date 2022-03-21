#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

import json
import sys
import os

# parse commmand line arguments
argument_list = str(sys.argv)

# create dict with input credentials and some more variables
json_credentials = {
    "type": "service_account",
    "project_id": os.environ["PROJECT_ID"],
    "private_key_id": os.environ["PRIVATE_KEY_ID"],
    "private_key": os.environ["PRIVATE_KEY"],
    "client_email": os.environ["CLIENT_EMAIL"],
    "client_id": os.environ["CLIENT_ID"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": argument_list[5],
}

print(json_credentials)

# write to JSON file
with open("./apecs-remote-sensing-database-e3d1516b4935.json", "w") as fp:
    json.dump(json_credentials, fp)
