import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().random,
    "pn": "382424",
    "mpid": "GROCERY"
}


def flipkartMarketplace(query):

    # data = {
    #     "locationContext":
    #     {
    #         "pincode": "395006"
    #     },
    #         "marketplaceContext": {"marketplace": "GROCERY"}}

    url = f'https://www.flipkart.com/'

    req = requests.get(url, headers=headers)

    sor = BeautifulSoup(req.text, "html.parser")

    return sor
