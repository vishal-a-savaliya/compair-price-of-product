import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().random
}


def flipkart(search):

    # print('flipkart')

    url = f'https://www.flipkart.com/search?q={search}'

    # Sending HTTP request
    req = requests.get(url, headers=headers)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    data = sor.findAll('div', {"class": "_4ddWXP"})

    result = []

    for item in data:

        try:
            product_link = "https://www.flipkart.com" + item.a['href']

        except:
            product_link = None

        try:
            product_image = item.a.div.div.div.img['src']
        except:
            product_image = None

        try:
            product_title = item.a.div.div.div.img['alt']
        except:
            product_title = None

        try:

            div = item.find_all('div', class_='_2D5lwg')[0]
            product_ratings = div.span.div.get_text()
            total = div.find_all('span')[1].get_text()

            total_users = total[1:-1]

        except:
            product_ratings = None

        try:
            product_price = item.find_all('a')[2].div.div.get_text()
            product_price = float(product_price[1:])
        except:
            product_price = None

        try:
            product_delivery = item.select_one('div ._2Tpdn3').get_text()

        except:
            product_delivery = None

        resultset = {
            'title': product_title,
            'image': product_image,
            'link': product_link,
            'price': product_price,
            'source': 'flipkart.com',
            'rating': product_ratings,
            'reviews': total_users,
            'delivery': product_delivery,

        }

        result.append(resultset)

    if result == []:

        for item in sor.select("._1fQZEK"):

            try:

                product_link = "https://www.flipkart.com" + item['href']

            except:
                product_link = None

            try:

                image_tag = item.select_one('div .CXW8mj').img
                product_image = image_tag['src']

                product_title = image_tag['alt']

            except:
                product_image = None
                product_title = None

            try:
                product_rating = item.select_one('div ._3LWZlK').text

            except:
                product_rating = None

            try:
                product_reviews = item.select_one(
                    "._2_R_DZ").span.span.text.split(" ")[0]

            except:
                product_reviews = None

            try:
                product_price = item.select_one(
                    'div ._30jeq3').text[1:]

                product_price = float(product_price.replace(',', ''))

            except:
                product_price = None

            try:
                product_delivery = item.select_one(
                    'div ._2Tpdn3').text
            except:
                product_delivery = None

            product = {
                'title': product_title,
                'image': product_image,
                'link': product_link,
                'price': product_price,
                'source': 'flipkart.com',
                'rating': product_rating,
                'reviews': product_reviews,
                'delivery': product_delivery,
            }

            result.append(product)

    return result
