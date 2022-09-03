from concurrent.futures import ThreadPoolExecutor

import json

from googleproduct import getProducts
from modules.flipkart import flipkart
from modules.meesho import meesho
from modules.shopclues import shopclues


import time

from modules.snapdeal import snapdeal


site_to_search = [getProducts, flipkart, shopclues, meesho, snapdeal]

threads = []
result = []
threads_results = []


def all_site_product(query):

    with ThreadPoolExecutor() as executor:

        # s1 = time.perf_counter()
        # t1 = executor.submit(flipkart, query)

        # t3 = executor.submit(getProducts, query)

        # t2 = executor.submit(shopclues, query)

        # result.append(t1.result())
        # result.append(t2.result())
        # result.append(t3.result())

        # f1 = time.perf_counter()

        # print(f's1 time is {round(f1-s1,2)} sec')

        for site in site_to_search:

            thrd = executor.submit(site, query)

            threads.append(thrd)

        for res in threads:
            result.append(res.result())

        # thread_results = executor.map(site_to_search, "power bank")

        # for site in site_to_search:
        #     thr = executor.submit(site, query)
        #     threads_results.append(thr)

        # for res in threads_results:
        #     result.append(res.result())

# for site in sites:
#         if site == 'flipkart':
#             t1 = threading.Thread(target=flipkart, args=['redmi note 6 pro'])

#             result.append({'flipkart': t1})

#             treads.append(t1)

#         if site == 'shopclues':
#             t2 = threading.Thread(target=shopclues, args=['laptop'])

#             result.append({'shopclues': t2})

#             treads.append(t2)

#     for tread in treads:
#         tread.join()


# all_site_product()
# print(result)

    # result.clear()

    # s2 = time.perf_counter()
    # for site in site_to_search:
    #     res = site(query)

    #     result.append(res)
    # f2 = time.perf_counter()

    # print(f's2 time is {round(f2-s2,2)} sec')

    return json.dumps(result)
