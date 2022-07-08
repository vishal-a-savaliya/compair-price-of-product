import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"
}

def flipkart(search):
        
        
        print('flipkart')  

        url = f'https://www.flipkart.com/search?q={search}'
        # url = f'https://www.amazon.in/s?k=vi+mifi&crid=397Z6HMC65FDQ&sprefix=vi+mi%2Caps%2C454&ref=nb_sb_ss_ts-doa-p_1_5'

        # Sending HTTP request
        req = requests.get(url, headers=headers)

        # Pulling HTTP data from internet
        sor = BeautifulSoup(req.text, "html.parser")

        # print(sor)
        data = sor.findAll('div', {"class": "_4ddWXP"})
        # data = sor.findAll('div')

        result = []

        for item in data:
            
            # print(len(item), item)

            try:
                image = item.a.div.div.div.img['src']
            except:
                image = None
            
            try:
                text = item.a.div.div.div.img['alt']
            except:
                text = None
            
            try:

                div = item.find_all('div', class_='_2D5lwg')[0]
                rate = div.span.div.get_text()
                total = div.find_all('span')[1].get_text()
                
                total = total[1:-1]
            
                ratings ={'rating':rate,'users':total}



            except:
                ratings = None
            
            # print('ratings->', item.find_all('div', class_='_2D5lwg')[0].span[1].get_text())


            try:
                price = item.find_all('a')[2].div.div.get_text()
            except:
                price = None

            # print("price->", item.find_all('a')[2].div.div.get_text())

            # if image and search.upper() in text.upper() :
            resultset ={'image': image, 'text': text ,'ratings':ratings,'price':price }

            result.append(resultset)


        return result   

print(flipkart("laptop"))