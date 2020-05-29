#!/usr/bin/python3
import requests
import json
import sys
from os import environ
import time
import configparser 

config = configparser.ConfigParser() 
config.read("settings.ini")
api_key=(config["api.websa.com"]["api_key"])

certbot_domain = environ["CERTBOT_DOMAIN"]
certbot_validation = environ["CERTBOT_VALIDATION"]

response = requests.get("https://api.websa.com/api/v1/dns_zones?page=1&q%5Bsorts%5D=updated_at+desc", headers={"X-Auth-Token":api_key})
JsonData = json.loads(response.text)

for i in JsonData["dns_zones"]:
    if i["name"] == certbot_domain:
    	dns_zone_id=i["id"]

requests.put(("https://api.websa.com/api/v1/dns_zones/%s" %(dns_zone_id)), 
	data=('{"dns_zone":{"records":[{"id":"","name":"_acme-challenge","ttl":60,"type":"TXT","priority":null,"weight":null,"port":null,"value":"%s"}]}}' %(certbot_validation))   , 
	headers={"Content-Type":"application/json","X-Auth-Token":api_key })

time.sleep(30)
