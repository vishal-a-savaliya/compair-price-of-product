
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def jiomart(query):

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

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.jiomart.com')

    sleep(2)

    # location = driver.find_element(By.ID, 'delivery_details')
    # location.send_keys(Keys.ENTER)

    # location_input = driver.find_elements(By.ID, 'rel_pincode')[0]

    # print(location_input)

    pincode = "382424"
    # location_input.clear()
    # location_input.setAttribute("value", pincode)
    # location_input.send_keys(pincode)
    # location_input.send_keys(Keys.ENTER)

    # input = driver.find_element(By.CLASS_NAME, 'aa-InputWrapper')
    input = driver.find_element(
        By.XPATH,  ".//*[@class='aa-Input input-text']")

    input.send_keys('bone vita')
    input.send_keys(Keys.ENTER)

    sleep(5)

    # search = driver.find_element(By.ID, 'input')

    # search.send_keys(query)

    # search.send_keys(Keys.ENTER)
    # # driver.get_screenshot_as_file('ss.png')

    # print('sleeping...')
    sleep(1)

    res = driver.find_elements(
        By.XPATH, ".//div[@class='']")

    # print(res)

    result = []

    for item in res:

        try:
            product_image = item.find_element(
                By.XPATH, ".//*[@class='']")

            # print("image: ", product_image)

        except:
            product_image = None

        try:
            product_title = item.find_element(
                By.XPATH, ".//*[@class='']")

            product_link = item.find_element(
                By.XPATH, ".//*[@class='']")

        except:
            product_title = None
            product_link = None

        try:
            product_price = item.find_element(
                By.XPATH, ".//*[@class='']")

        except:
            product_price = None

        try:
            product_rating = item.find_element(
                By.XPATH, ".//*[@class='']")

        except:
            product_rating = None

        try:
            product_reviews = item.find_element(
                By.XPATH, ".//*[@class='']")

        except:
            product_reviews = None

        product = {

            'title': product_title,
            'image': product_image,
            'link': product_link,
            'price': product_price,
            'source': 'jiomart',
            'rating': product_rating,
            'reviews': product_reviews,
            'delivery': None,

        }

        result.append(product)

    driver.close()

    return json.dumps(result)


# jiomart("nothing")
