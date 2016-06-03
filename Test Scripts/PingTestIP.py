#!/usr/bin/env python
# This script checks to see if the server is up or down. 

import requests
import socket
import time

while True:
    
    host = 'http://ssmale.ddns.net'
    
    ip = socket.gethostbyname('ssmale.ddns.net')
    
    print ip
        
    response = requests.get(host)
    if response.status_code == requests.codes.ok:
        print('Server Up')
    else:
        print('Server Down')
    time.sleep(10)