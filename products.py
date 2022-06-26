from audioop import getsample
import requests
import json
from bs4 import BeautifulSoup
from sites import getSite


search = 'power bank'

sites = getSite(search)

for s in sites:

    if s['site'] == 'amazon':

        # print('amazon')

        url = f'https://www.amazon.in/s?k={search}'

        # Sending HTTP request
        req = requests.get(url)

        # Pulling HTTP data from internet
        sor = BeautifulSoup(req.text, "html.parser")

        # Finding temperature in Celsius
        data = sor.findAll('div', {"class": "sg-row"})

        for item in data:

            print(item)
            # try:
            #     url = item.parent['href'].split('https')[1]

            # except:
            #     url = None

            # if url:
            #     tsd, td, tsu = extract("https"+url)
            #     sites = td
            #     list.append({'site': sites})
