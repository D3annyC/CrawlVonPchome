import requests
import re
import json


class ProductSeek:
    def __init__(self, kw):
        self.kw = kw
        surl = 'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q='
        res = requests.get(surl+kw)
        res_text = res.text
        global jd
        jd = json.loads(res_text)

    def result(self):
        try:
            products = []
            prices = []
            urls = []
            main_url = 'http://24h.pchome.com.tw/prod/'
            for item in jd['prods']:
                products.append(item['name'])
                prices.append(item['price'])
                url = main_url+item['Id']
                urls.append(url)

            for item in products:
                print(item)
        except:
            print('糟糕，您要找的商品可能被新台幣下架了!')


if __name__ == "__main__":
    keyWords = input("今天想敗甚麼呢： ")
    search = ProductSeek(keyWords)
    search.result()
