#!/usr/bin/env python
# This script checks to see if the server is up or down. 
# This info will then be written to a mysql db

import MySQLdb
import requests
import time

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="ping",         # your username
                     passwd="websiteping",  # your password
                     db="Ping")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

while True:
    response = requests.get('http://ssmale.ddns.net', stream=True)
    ip = response.raw._connection.sock.getpeername()
    if response.status_code == requests.codes.ok:
        print('Server Up')
        cur.execute("INSERT INTO `Ping`.`ping_history` (`ping_id`, `status`) VALUES ('%s', 'Live')", ip)
    else:
        print('Server Down')
        cur.execute("INSERT INTO `Ping`.`ping_history` (`ping_id`, `status`) VALUES ('%s', 'Down')", ip)
    time.sleep(10)