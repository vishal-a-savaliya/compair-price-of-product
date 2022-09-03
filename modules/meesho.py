import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {
    "User-Agent": UserAgent().random
}


def meesho(search):

    # print('meesho')

    url = f'https://www.meesho.com/search?q={search}'

    # Sending HTTP request
    req = requests.get(url, headers=headers)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    result = []

    for item in sor.select(".sc-dkPtyc "):

        try:
            product_link = item.select_one('a')['href']
            product_link = 'https://www.meesho.com' + product_link

        except:
            product_link = None

        product_div = item.select_one('div')

        try:
            product_title = product_div.select(
                'div')[1].p.text
        except:
            product_title = None

        try:
            product_image = product_div.select(
                'div')[0].picture.source['srcset']

        except:
            product_image = None

        try:
            price_tag = product_div.select(
                'div')[1].select('div')[0]

            price_tag = price_tag.h5.text

            product_price = price_tag

        except:
            product_price = None

        try:

            rating_tag = product_div.select('div')[1].select('div')[
                4].select('span')

            product_rating = float(rating_tag[0].span.text)
            product_reviews = rating_tag[2].text

            if product_reviews == 'Supplier':
                product_reviews = None
            else:
                product_reviews = product_reviews.split(' ')[0]

        except:
            product_rating = None
            product_reviews = None

        try:
            delivery_tag = product_div.select('div')[1].select('div')[2]
            product_delivery = delivery_tag.span.text

        except:
            product_delivery = None

        if product_title is not None and product_price is not None:

            resultset = {

                'title': product_title,
                'image': product_image,
                'link': product_link,
                'price': product_price,
                'source': 'meesho.com',
                'rating': product_rating,
                'reviews': product_reviews,
                'delivery': product_delivery,

            }

            result.append(resultset)

    return result
