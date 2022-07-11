import requests
from bs4 import BeautifulSoup
from googleproduct import getProducts


def getProductName(query):

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    params = {"hl": "en", 'gl': 'in'}
    cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}

    response = requests.get(f"https://www.google.com/search?q={query}",headers=headers,cookies=cookies)

    soup = BeautifulSoup(response.text, 'html.parser')


    for item in soup.findAll('h3'):

        try:
            product = item.text
        except:
            product = None

        if(product!=None):
            # print(product)
            return getProducts(product)
            
    if product == None:
        return getProducts(query)    
        

# print(getProductName(8901030865237))
