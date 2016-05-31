#!/usr/bin/env python
# This script checks to see if the server is up or down. 

import requests
import time

while True:
    response = requests.get('http://ssmale.ddns.net')
    if response.status_code == requests.codes.ok:
        print('Server Up')
    else:
        print('Server Down')
    time.sleep(10)