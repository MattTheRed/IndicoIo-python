"""
Basic configuration for the indico API wrapper.
"""

import os.path
import json

local_api_root = "http://localhost:9438/"
api_root = "http://apiv1.indico.io/"

try:
	directory = os.path.dirname(__file__)
	auth_file = os.path.abspath(os.path.join(directory, "config.json"))
	auth = json.load(open(auth_file))
except IOError, ValueError:
    auth = {
        "INDICO_EMAIL": None,
        "INDICO_PASSWORD": None
    }
