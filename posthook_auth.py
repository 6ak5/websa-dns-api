#!/usr/bin/python3

import requests
import json
import sys
from os import environ
import time
import configparser
import tldextract

config = configparser.ConfigParser()
config.read("settings.ini")
api_key = config["api.websa.com"]["api_key"]

certbot_domain = environ["CERTBOT_DOMAIN"]
certbot_validation = environ["CERTBOT_VALIDATION"]

extract = tldextract.TLDExtract(include_psl_private_domains=True)
extracted_domain = extract(certbot_domain)

subdomain = extracted_domain.subdomain
target_domain = extracted_domain.domain + "." + extracted_domain.suffix

response = requests.get("https://api.websa.com/api/v1/dns_zones?page=1&q%5Bsorts%5D=updated_at+desc", headers={"Authorization": api_key})
JsonData = json.loads(response.text)

for i in JsonData["dns_zones"]:
    if i["name"] == target_domain:
        dns_zone_id = i["id"]

acme_challenge_name = "_acme-challenge"
if subdomain:
    acme_challenge_name += "." + subdomain

data = {
    "dns_zone": {
        "records": [
            {
                "id": "",
                "name": acme_challenge_name,
                "ttl": 60,
                "type": "TXT",
                "priority": None,
                "weight": None,
                "port": None,
                "value": certbot_validation
            }
        ]
    }
}

requests.put(
    "https://api.websa.com/api/v1/dns_zones/%s" % dns_zone_id,
    data=json.dumps(data),
    headers={"Content-Type": "application/json", "Authorization": api_key}
)

time.sleep(30)

