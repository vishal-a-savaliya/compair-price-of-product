import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent




headers = {
    "User-Agent": UserAgent().random
}


def amazon(search):

    print('amazon')

    url = f'https://www.amazon.in/s?k={search}'
    #     url = f'https://www.amazon.in/s?k=vi+mifi&crid=397Z6HMC65FDQ&sprefix=vi+mi%2Caps%2C454&ref=nb_sb_ss_ts-doa-p_1_5'

    #Sending HTTP request
    req = requests.get(url, headers=headers)

    # Pulling HTTP data from internet
    sor = BeautifulSoup(req.text, "html.parser")

    print(sor)
    data = sor.findAll('div', {"class": "sg-row"})
    # data = sor.findAll('div')

    result=[]

    for item in data:

        try:
                image = item.find(class_='s-image')['src']
                text = item.find(class_='s-image')['alt']

                span = item.find_all('span', attrs={"aria-label": True})
                ratings = span['aria-label'][0]
                print(span, ratings)

        except:
                image = None
                text = None

        if image and search.upper() in text.upper() :
            print({'image': image, 'text': text})

    return result


print(amazon("mi+band+6"))
