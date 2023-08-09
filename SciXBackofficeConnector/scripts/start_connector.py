import requests
import json
import os

request_header = {"Accept": "application/json", "Content-Type": "application/json"}
connector_config_path = ""
connector_data = json.load(connector_config_path)

requests.post(url=os.getenv['CONNECTOR_URL'], headers=request_header, data=connector_data)