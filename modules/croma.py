from weakref import proxy
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# px = requests.get("https://gimmeproxy.com/api/getProxy?country=IN")

# pxdata = px.json()

# ip=pxdata['ipPort']

headers = {
    "User-Agent": UserAgent().random
}


def croma(search):
 
    print('croma')

    url = f'https://www.croma.com/search/?q={search}'

    # Sending HTTP request
    req = requests.get(url,headers=headers)
    # proxies = {"http": ip, "https": ip}

    print(req.status_code)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    print(sor)
    data = sor.findAll('div', {"class": "cp-product"})

    print(data)

    result = []

    for item in data:

        print(len(item), item)

        try:
            div = item.find_all(div, class_="product-img")[0]
            image = item.a.img['src']

            print(image)

        except:
            image = None

        try:
            div = item.find_all(div, class_="product-img")[0]
            text = item.a.img['alt']
        except:
            text = None

        div = item.find_all('div', class_='product-info')[0]

        try:

            idiv = div.find_all('div', class_='cp-rating')
            rate = idiv[0].fieldset.span['aria-label']
            total = idiv[0].span.get_text()

            # total = total[1:-1]

            ratings = {'rating': rate, 'users': total}

        except:
            ratings = None

        # print('ratings->', item.find_all('div', class_='_2D5lwg')[0].span[1].get_text())

        try:

            idiv = div.find_all('div', class_='cp-price')
            price = idiv[0].span.span.get_text()
        except:
            price = None

        # print("price->", item.find_all('a')[2].div.div.get_text())

        if image and search.upper() in text.upper():
            resultset = {'image': image, 'text': text,
                         'ratings': ratings, 'price': price}

            print(resultset)
            result.append(resultset)

    return result


print(croma('power bank'))
