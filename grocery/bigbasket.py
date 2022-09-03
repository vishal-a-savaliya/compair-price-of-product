
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def bigbasket(query, pincode="560008"):

    user_agent = UserAgent().random

    options = webdriver.ChromeOptions()

    options.headless = True

    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    # _options = webdriver.ChromeOptions()
    # _options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)
    driver.get('https://www.bigbasket.com')

    # attempts = 0

    # location = None

    # while attempts < 5:
    #     try:
    #         location = driver.find_element(
    #             By.XPATH, ".//*[@class='dropdown new-to-bb xhrcalls-only']/a")
    #         break
    #     except:
    #         sleep(1)
    #         attempts += 1

    # # print(location.get_attribute('innerHTML'))
    # location.click()

    # enter_pincode = driver.find_element(
    #     By.XPATH, ".//div[@class='form-group area-autocomplete area-select ng-scope']/input")

    # # enter_pincode = enter_pincode.find_elemnt(By.TAG_NAME, 'input')

    # pincode = "380059"

    # enter_pincode.send_keys(pincode)
    # sleep(10)

    # try:
    #     enter_pincode.send_keys(Keys.ENTER)
    # except:
    #     print("pincode is not available")
    #     # return []

    search = driver.find_element(By.ID, 'input')

    # query = "tomato"
    search.send_keys(query)

    search.send_keys(Keys.ENTER)
    # driver.get_screenshot_as_file('ss.png')

    # print('sleeping...')
    sleep(1)

    res = driver.find_elements(
        By.XPATH, ".//div[@class='item prod-deck row ng-scope']")

    # print(res)

    result = []

    for item in res:

        try:
            product_image = item.find_element(
                By.XPATH, ".//*[@class='img-responsive blur-up lazyautosizes lazyloaded']").get_attribute("src")

            # print("image: ", product_image)

        except:
            product_image = None

        try:
            product_title = item.find_element(
                By.XPATH, ".//*[@class='col-sm-12 col-xs-7 prod-name']/a").text

            product_link = item.find_element(
                By.XPATH, ".//*[@class='col-sm-12 col-xs-7 prod-name']/a").get_attribute("href")

            if product_title.lower().find(query.lower()) == -1:
                continue

        except:
            product_title = None
            product_link = None

        try:
            product_price = item.find_element(
                By.XPATH, ".//*[@class='discnt-price']")

            product_price = product_price.find_element(
                By.CSS_SELECTOR, 'span:last-child').text

        except:
            product_price = None

        try:
            product_rating = item.find_element(
                By.XPATH, ".//*[@class='col-sm-12 col-xs-7 prod-name']/div/span").text

        except:
            product_rating = None

        try:
            product_reviews = item.find_element(
                By.XPATH, ".//*[@class='col-sm-12 col-xs-7 prod-name']/div/span[2]").text

            product_reviews = product_reviews.split(' ')[0]

        except:
            product_reviews = None

        product = {

            'title': product_title,
            'image': product_image,
            'link': product_link,
            'price': product_price,
            'source': 'Bigbasket.com',
            'rating': product_rating,
            'reviews': product_reviews,
            'delivery': None,

        }

        # print(product)
        result.append(dict(product))

    driver.close()

    return result
