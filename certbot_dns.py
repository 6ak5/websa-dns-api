#!/usr/bin/python3
import sys
import subprocess
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
email=(config["api.websa.com"]["email"])

with open(r"domain-list.conf", "r") as file:
    for line in file:
        certbot = subprocess.call([
            "certbot",
            "--text",
            "--agree-tos",
            "--email", email,
            "-d", line,
            "--manual-auth-hook", "./posthook_auth.py",
            "--manual-cleanup-hook", "./posthook_clean.py",
            "--manual",
            "--preferred-challenges", "dns",
            "--expand",
            "--renew-by-default",
            "--manual-public-ip-logging-ok",
            "certonly",
            "--dry-run"
            ])

