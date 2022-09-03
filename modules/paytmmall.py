import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {
    "User-Agent": UserAgent().random
}


def paytmmall(search):

    print('paytmmall')

    url = f'https://www.jiomart.com/catalogsearch/result?q={search}'

    # Sending HTTP request
    req = requests.get(url, headers=headers)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    return sor
    # data = sor.findAll('li', {"class": "ais-InfiniteHits-item"})
    # data = sor.findAll('div')

    result = []

    for item in sor.select("cat-item"):

        image = item.select_one('cat-img img')['src']

        # print(image)

    return result


print(jiomart("odomos"))
