#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import json
import os
import sys
from prefect import Flow, task

def run_actions():
    print("##### CHECK FOR ENV VALUES")
    mms_url = os.environ["MMS_URL"]
    print(f"Fetched MMS_URL value is {mms_url}")

    print("##### CHECK FOR INSTALLED REQUIREMENTS")

    print(f"Flow object is - {Flow.__dict__}")

    print("####### Add a sample file.")
    data = {
        "morguard": "en_ca",
        "hammerson": "fr_fr"
    }
    with open("sample_config.json", "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    run_actions()
