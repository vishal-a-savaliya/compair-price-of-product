from concurrent.futures import ThreadPoolExecutor, thread

import json
from googleSpecific import getProductsFromSite

from grocery.dmart import dmart
from grocery.bigbasket import bigbasket


result = []


def grocery(query, pincode):

    with ThreadPoolExecutor() as executor:

        t1 = executor.submit(dmart, query, pincode)

        t2 = executor.submit(bigbasket, query)

        t3 = executor.submit(getProductsFromSite, "jiomart", query)

        result.append(t1.result())
        result.append(t2.result())
        result.append(t3.result())

    return json.dumps(result)


# print(grocery("ghee", "382424"))
