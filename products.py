
# import attr
from matplotlib.pyplot import cla
import requests
import json
from bs4 import BeautifulSoup
from sites import getSite
from modules.flipkart import flipkart
from modules.amazon import amazon


search = 'power bank'

sites = getSite(search)

for s in sites:

    # if s == 'amazon':

    #     data = amazon(search)

    #     print(data)


    # if s == 'flipkart':

    #     data = flipkart(search)

    #     print(data)

    if s == 'croma':
         
         data =
