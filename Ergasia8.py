import json
import urllib.request
import sys

def get_coin_data(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms="+coin+"&tsyms=EUR&e=CCCAGG"
    d=json.loads(urllib.request.urlopen(url).read().decode())
    return d[coin]["EUR"]

def sec_check(coin):
    if (type(js.get(coin))!=int and type(js.get(coin))!=float) or (js.get(coin)<0):
        print("Λανθασμένη τιμή εισαγωγής", coin)
        sys.exit()

def third_check(coin):
    if coin in js:
        toEur=get_coin_data(coin)
        print("Ο χρήστης έχει",js.get(coin), coin, "που ισοτιμούν με",js.get(coin)*toEur,"€")
    else:
        print("Ο χρήστης δεν έχει", coin)

with open("erg8.txt") as f:
    data = f.read()
js=json.loads(data)
sec_check("BTC")
sec_check("ETH")
sec_check("LTC")
third_check("BTC")
third_check("ETH")
third_check("LTC")
