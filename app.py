from flask import *
from googleproduct import getProducts
from qr import getProductName
from sites import getSite

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to compare API"


@app.route('/search/<query>')
def search(query):
    return getProducts(query)
    # return str(getProducts(query))


@app.route('/sites/<query>')
def sites(query):
    return getSite(query)
    # return f"hiii this is {query}"

@app.route('/qr/<query>')
def qr(query):
    return getProductName(query)


if __name__ == '__main__':
    app.run(port=7777)
