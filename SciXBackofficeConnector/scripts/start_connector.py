import requests
import json
import os

request_header = {"Accept": "application/json", "Content-Type": "application/json"}
proj_home = os.path.abspath(os.path.join(__file__ ,"../.."))
connector_config_file=os.path.join(proj_home, "connect_config_files/register-postgres.json")
with open(connector_config_file) as f:
    connector_data = json.load(f)

resp = requests.post(\
    url=os.getenv("CONNECT_URL", "http://localhost:8083/connectors/"), \
    headers=request_header, \
    data=json.dumps(connector_data))

print(json.dumps(resp.json()))