# WELCOME TO COMPARE API 🔥🥤

---

The API provide you products from most used e-commerce site, you can request for product and API gives you products from all e-commerce site as response. including sites like Amazon, Flipkart, meesho, shopclus, snapdeal, and many more ...

You can also request for grocery product and API gives you pruducts from online grocery store as response including sites Dmart, Bigbasket, Jiomart and many more to come!

The API also provide the produts from products barcode, send barcode as request and as response you get the products releted to the barcode.

# RESPONSE FORMATE

```json
    [
         {

            "title": "product_title",
            "image": "product_image",
            "link": "product_link",
            "price": "product_price",
            "source": "site name",
            "rating": "product_rating",
            "reviews": "product_reviews",
            "delivery": "Product_delivery"
        },
    ]

```

# END POINTS

### **Get Product from All site**

return product list compine from all site serve

`https://cmp-api.vercel.app/all/<Search Query>`

#

### **Get Grocery Product from All site**

return grocery product from all sites we serve.

`https://cmp-api.vercel.app/grocery/<pincode>/<Search Query>`

#

### **Get products by Barcode No**

returns the products relevent to barcode No from all site having that product.

`https://cmp-api.vercel.app/qr/<Search Query>`

#

### **Get List of website where product is available**

returns the top websites name where product is available

`https://cmp-api.vercel.app/availableon/<Search Query>`

```json

    [
        "tatacliq",
        "gadgetsnow",
        "amazon",
        "qualitylogoproducts",
        "mysmartprice",
        "ambraneindia",
        "indiamart",
        "myg",
        "syska",
        "91mobiles",
        "paytmmall",
        "flipkart",
        "instructables",
        "nykaa"
    ]

```

#

### **Search products from single site**

returns the products available at site based on query

`https://cmp-api.vercel.app/site/<site name>/<Search Query>`

| website       | site name |
| ------------- | --------- |
| google.in     | google    |
| Flipkart.com  | flipkart  |
| meesho.com    | meesho    |
| snapdeal.com  | snapdeal  |
| shopclues.com | shopclues |

#

### **Search Grocery products from single site**

returns the products available on grocery site based on query

`https://cmp-api.vercel.app/grc/<site name>/<Search Query>`

| website       | site name |
| ------------- | --------- |
| Dmart.in      | dmart     |
| bigbasket.com | bigbasket |

### **Search products from any site**

returns the products available on site based on query

`https://cmp-api.vercel.app/specific/<site name>/<Search Query>`

**Use the site name as only name of the site:**

For Example

> www.xyz.com -> xyz

For best result you can use following table:

| website       | site name | website       | site name |
| ------------- | --------- | ------------- | --------- |
| tatacliq.com  | tatacliq  | Dmart.in      | dmart     |
| croma.com     | croma     | bigbasket.com | bigbasket |
| amazon.com    | amazon    | jiomart.com   | jiomart   |
| indiamart.com | indiamart | nykaa.com     | nykaa     |
| flipkart.com  | flipkart  | ajio.com      | ajio      |
| oneplus.in    | oneplus   | myntra.com    | myntra    |
| paytmmall.com | paytmmall | firstcry.com  | firstcry  |

