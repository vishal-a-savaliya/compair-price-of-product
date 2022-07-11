import requests
import json
from bs4 import BeautifulSoup


def getProducts(query):

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    params = {"hl": "en", 'gl': 'in', 'tbm': 'shop'}
    cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}

    response = requests.get(f"https://www.google.com/search?hl=en-IN&gl=IN&ceid=IN:en&q={query}",
                            params=params,
                            headers=headers,
                            cookies=cookies)

    soup = BeautifulSoup(response.text, 'html.parser')

    # return soup

    shopping_data = []
    inline_results_dict = {}
    shopping_results_dict = {}
    # images = {}

    for inline_result in soup.select('.sh-np__click-target'):

        inline_shopping_title = inline_result.select_one(
            '.sh-np__product-title').text
        inline_shopping_link = f"https://www.google.com{inline_result['href']}"
        inline_shopping_image = inline_result.div.img['src']

        inline_shopping_price = inline_result.select_one('b').text
        inline_shopping_price = inline_shopping_price.split(' ')[0]
        inline_shopping_price = inline_shopping_price.split('\xa0')[0]
        inline_shopping_price = inline_shopping_price.split('+')[0]
        inline_shopping_price = inline_shopping_price[1:]
        inline_shopping_price = float(inline_shopping_price.replace(',',''))

        inline_shopping_source = inline_result.select_one(
            '.E5ocAb').text.strip()

        inline_results_dict.update({

            'title': inline_shopping_title,
            'image': inline_shopping_image,
            'link': inline_shopping_link,
            'price': inline_shopping_price,
            'source': inline_shopping_source,
            'rating': None,
            'reviews': None,
            'delivery': None,

        })

        shopping_data.append(dict(inline_results_dict))

    for shopping_result in soup.select('.xcR77'):

        # print("working")

        try:
            title = shopping_result.select_one('.rgHvZc a').text
        except:
            title = None

        try:
            image = shopping_result.select_one('.oR27Gd img')['src']

        except:
            image = None

        try:
            product_link = f"https://www.google.com{shopping_result.select_one('.rgHvZc a')['href']}"
        except:
            product_link = None

        try:
            source = shopping_result.select_one('span.HRLxBb').next_sibling.split(' ')[-1]
        except:
            source = None

        try:
            price = shopping_result.select_one('span.HRLxBb').text
            price = price.split(' ')[0]
            price = price.split('\xa0')[0]
            price = price.split('+')[0]
            price = price[1:]
            price = float(price.replace(',',''))

        except:
            price = None

        

        try:
            rating = shopping_result.select_one('.m0amQc.DApVsf')[
                'aria-label'].split(' ')[0]
        except:
            rating = None

        try:
            reviews = shopping_result.select_one(
                '.dD8iuc.d1BlKc span').text

            reviews = reviews[1:-1]
        except:
            reviews = None

        try:
            delivery = shopping_result.select_one('span.dD8iuc').text
        except:
            delivery = None

        if title and image and product_link :
            shopping_results_dict.update({

                'title': title,
                'image': image,
                'link': product_link,
                'price': price,
                'source': source,
                'rating': rating,
                'reviews': reviews,
                'delivery': delivery,

            })

            shopping_data.append(dict(shopping_results_dict))
            # print(dict(shopping_results_dict))

    # shopping_data.sort(key=lambda x: x["price"].lower())
    shopping_data = sorted(shopping_data, key=lambda d: d['price'])
    # print(shopping_data)

    
    
    return json.dumps(shopping_data, indent=2, ensure_ascii=False)


    # return shopping_data


# print(getProducts('colgate'))
