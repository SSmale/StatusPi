import requests
import time

while True:
    response = requests.get('http://ssmale.ddns.net')
    if response.status_code == requests.codes.ok:
        print('Server Up')
    else:
        print('Server Down')
    time.sleep(10)