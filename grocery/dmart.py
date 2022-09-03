
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def dmart(query, pincode="400053"):

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

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://www.dmart.in/')

    attempts = 0

    pin = None

    while attempts < 5:
        try:
            pin = driver.find_element(By.ID, 'pincodeInput')
            break
        except:
            sleep(1)
            attempts += 1

    if pin is None:
        # print("return from pin")
        return []

    pin.send_keys(pincode)

    select_pincode = driver.find_element(
        By.XPATH, ".//div[@class='src-client-components-pincode-widget-__pincode-widget-module___listdiv']")

    attempts = 0
    while attempts < 3:
        try:
            button = select_pincode.find_element(
                By.TAG_NAME, 'button').send_keys(Keys.ENTER)
            break

        except:
            if attempts == 2:
                # location is lot available
                print("return bc pin is lot available")
                return []

            sleep(1)
            attempts += 1

    try:
        ok = driver.find_element(
            By.XPATH, ".//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-6']/button").send_keys(Keys.ENTER)
    except:
        # print("ok button")
        return []

    sleep(2)
    input = driver.find_element(
        By.XPATH, ".//div[@class='src-client-components-header-components-search-__search-module___src-backdrop-cntr']")

    input = input.find_element(By.TAG_NAME, 'input')

    input.send_keys(query)

    input.send_keys(Keys.ENTER)

    sleep(5)

    attempts = 0
    grid = None

    while attempts < 5:

        try:
            grid = driver.find_element(
                By.XPATH, ".//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-1']")
            break

        except:
            sleep(1)
            attempts += 1

    if grid is None:
        # print("grid not found!")
        return []

    attempts = 0

    res = None

    while attempts < 3:

        try:
            res = grid.find_elements(
                By.XPATH, ".//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-auto MuiGrid-grid-xl-auto']/div")
            break
        except:
            attempts += 1
            sleep(1)

    if res is None:
        # print("res is not found")
        return []

    result = []

    for item in res:

        try:
            product_title = item.find_element(
                By.XPATH, ".//a[@class='src-client-components-product-card-vertical-card-__vertical-card-module___title']").text

            if product_title.lower().find(query.lower()) == -1:
                continue

        except:
            product_title = None

        try:
            product_image = item.find_element(
                By.XPATH, ".//div[@class='src-client-components-product-card-vertical-card-__vertical-card-module___section-top']/a/div")

            styles = product_image.value_of_css_property(
                'background-image')

            product_image = styles.split('"')[1]

        except:
            product_image = None

        try:
            product_link = item.find_element(
                By.XPATH, ".//div[@class='src-client-components-product-card-vertical-card-__vertical-card-module___section-top']/a").get_attribute("href")

        except:
            product_link = None

        try:
            product_price = item.find_elements(
                By.XPATH, ".//span[@class='src-client-components-product-card-vertical-card-__vertical-card-module___amount']")[1].text

        except:
            product_price = None

        product_rating = None
        product_reviews = None

        product = {

            'title': product_title,
            'image': product_image,
            'link': product_link,
            'price': product_price,
            'source': 'Dmart.in',
            'rating': product_rating,
            'reviews': product_reviews,
            'delivery': None,

        }

        # print(product)

        result.append(dict(product))

    driver.close()

    # print("finall result")
    return result
