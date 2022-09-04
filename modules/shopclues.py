import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {
    "User-Agent": UserAgent().random
}


def shopclues(search):

    print('shopclues')

    url = f'https://bazaar.shopclues.com/search?q={search}'

    # Sending HTTP request
    req = requests.get(url, headers=headers)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    result = []

    for item in sor.select(".column"):

        atag = item.select_one('a')
        link = f"https:{atag['href']}"

        try:
            image = atag.select_one('.img_section').img['src']

            if "https" not in image:
                image = f"https:{image}"

        except:
            image = None

        try:
            title = atag.select_one('.img_section').img['alt']
        except:
            title = None

        try:
            price = atag.select_one(
                'div .new_prd_section').div.span.text

            price = price.strip()
            price = price[1:]
            price = float(price.replace(',', ''))

        except:
            price = None

        if title is not None and image is not None and price is not None:
            resultset = {

                'title': title,
                'image': image,
                'link': link,
                'price': price,
                'source': 'shopclues.com',
                'rating': None,
                'reviews': None,
                'delivery': None,

            }

            result.append(resultset)

    return result
