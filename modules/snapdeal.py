import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {
    "User-Agent": UserAgent().random
}


def snapdeal(search):

    print('snapdeal')

    url = f'https://www.snapdeal.com/search?keyword={search}'

    # Sending HTTP request
    req = requests.get(url, headers=headers)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    result = []

    for item in sor.select(".product-tuple-listing"):

        try:
            product_link = item.select_one('a')['href']

        except:
            product_link = None

        try:
            product_title = item.select_one(
                'div .product-desc-rating ').a.p.text
        except:
            product_title = None

        try:
            img_tag = item.select_one('.product-tuple-image').a.picture.source
            product_image = img_tag['srcset']

        except:
            product_image = None

        try:
            price_tag = item.select_one('div .product-desc-rating ').a

            price_tag = price_tag.select_one(
                'div .product-price-row').select_one('div .lfloat')

            price_tag = price_tag.select('span')[1]['data-price']

            product_price = float(price_tag)

        except:
            product_price = None

        try:

            rating_tag = item.select_one('div .product-desc-rating').a
            rating_tag = rating_tag.select_one(
                'div .rating').div.select_one('div .filled-stars')

            rating_tag = rating_tag['style'].split(':')[1]
            rating_tag = rating_tag[:-1]

            product_rating = float(rating_tag)*5/100

        except:
            product_rating = None

        try:
            reviews_tag = item.select_one('div .product-desc-rating').a
            reviews_tag = reviews_tag.select_one('div .rating').p.text

            reviews_tag = reviews_tag[1:-1]

            product_reviews = reviews_tag

        except:
            product_reviews = None

        resultset = {

            'title': product_title,
            'image': product_image,
            'link': product_link,
            'price': product_price,
            'source': 'snapdeal.com',
            'rating': product_rating,
            'reviews': product_reviews,
            'delivery': None,

        }

        result.append(resultset)

    return result
