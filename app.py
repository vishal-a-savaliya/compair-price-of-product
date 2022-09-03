
from flask import *
import json
from flask_caching import Cache

from googleSpecific import getProductsFromSite
from googleproduct import getProducts
from allSitesProduct import allSitesProduct
from qr import getProductName
from getAvailableOnSites import getAvailableOnSites

from modules.shopclues import shopclues
from modules.meesho import meesho
from modules.flipkart import flipkart
from modules.snapdeal import snapdeal


from grocery.flipkartMarketpalce import flipkartMarketplace
from groceryProducts import grocery
from grocery.jiomart import jiomart
from grocery.dmart import dmart
from grocery.bigbasket import bigbasket


sites = {
    "shopclues": shopclues,
    "meesho": meesho,
    "flipkart": flipkart,
    "snapdeal": snapdeal,
    "google": getProducts
}

grocerySites = {
    "dmart": dmart,
    "bigbasket": bigbasket
}


cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

app = Flask(__name__)

cache.init_app(app)


@app.route("/")
def home():
    return "Welcome to compare API"


@app.route('/google/<query>')
def search(query):
    return json.dumps(getProducts(query))


@app.route('/availableon/<query>')
def getAvailableOnSites(query):
    return getAvailableOnSites(query)


@app.route('/qr/<query>')
def qr(query):
    return getProductName(query)


@app.route('/all/<query>')
@cache.cached(timeout=1000)
def allProducts(query):
    return allSitesProduct(query)


@app.route('/site/<site_name>/<query>')
def getResultFrom(site_name, query):
    try:
        website = sites[site_name]
    except:
        return "Site not found!"
    return json.dumps(website(query))


@app.route('/grc/<site_name>/<pincode>/<query>')
@cache.cached(timeout=1000, unless=[])
def getGroceryFrom(site_name, query, pincode):
    try:
        grocery_site = grocerySites[site_name]
    except:
        return "Site not found!"
    result = json.dumps(grocery_site(query, pincode))
    return result


@app.route('/grocery/<pincode>/<query>')
@cache.cached(timeout=1000, unless=[])
def getgrocery(query, pincode):
    grocery_result = grocery(query, pincode)
    return json.dumps(grocery_result)


@app.route('/specific/<site>/<query>')
def getspefic(site, query):
    return getProductsFromSite(site, query)


@app.route('/fm/<query>')
def getfm(query):
    return str(flipkartMarketplace(query))


if __name__ == '__main__':
    app.debug = True
    app.run(port=7777)
