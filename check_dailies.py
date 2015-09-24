#!/usr/bin/python

import requests
import json
import datetime
import sys
from os.path import expanduser

def getIncompleteTaskCount(apiuuid, apikey):
    r = requests.get("https://habitica.com:443/api/v2/user/tasks", headers = { "x-api-key" : apikey, "x-api-user" : apiuuid })

    tasks = json.loads(r.text)

    habitica_wdaynames = [ "m", "t", "w", "th", "f", "s", "su"]

    dayofweek = habitica_wdaynames[datetime.datetime.today().weekday()]

    incomplete_tasks = 0

    for task in tasks:
        if task["type"] == "daily" and not task["completed"] and task["repeat"][dayofweek]:
            incomplete_tasks += 1

    return incomplete_tasks

def main():
    cfg_fname = expanduser("~/.habitica")
    cfg_file = open(cfg_fname, "r")
    cfg = json.loads(cfg_file.read())
    cfg_file.close()

    incomplete_tasks = getIncompleteTaskCount(cfg["uuid"], cfg["token"])
    if incomplete_tasks > 0:
        print incomplete_tasks
        sys.exit(1)

if __name__ == "__main__":
    main()
