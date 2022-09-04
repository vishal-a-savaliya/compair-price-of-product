from concurrent.futures import ThreadPoolExecutor

import json

from googleproduct import getProducts
from modules.flipkart import flipkart
from modules.meesho import meesho
from modules.shopclues import shopclues


from modules.snapdeal import snapdeal


site_to_search = [getProducts, flipkart, shopclues, meesho, snapdeal]

threads = []
result = []


def allSitesProduct(query):

    with ThreadPoolExecutor() as executor:

        for site in site_to_search:

            thrd = executor.submit(site, query)

            threads.append(thrd)

        for res in threads:

            if len(res.result()) > 0:
                result.append(res.result())

    return json.dumps(result)
