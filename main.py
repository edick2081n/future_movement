import requests
import json
import time
from process import process_data

#  В качестве допущения, принимаю, что движения фьючерса ETH относитьельно USDT повторяет движение фьючераса
#  BTC относительно USDT в процентном соотношении с задержкой на 5 минут
# В случае если движение ETH отличается от вышеуказанного движения BTC в ту или иную сторону, то  такое движение,
# рассматривую как собственное движение  фьючерса ETH
# В качестве отслеживаемых параметров выбираю следующие: markPrice ( текущая цена сделки) и time (время совершения
# сделки)


file1 = open('ethusdt.txt', 'a')
file2 = open('btcusdt.txt', 'a')

while True:
    #response = requests.post("https://data.binance.com/api/v3/ticker/price", {"symbol":"ETHUSDT"}, header={"X-MBX-APIKEY": "34" })
    response1 = requests.get("https://www.binance.com/fapi/v1/premiumIndex?symbol=ETHUSDT")
    response2 = requests.get("https://www.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT")
    #a = response1.content
    data1 = json.loads(response1.content)
    data2 = json.loads(response2.content)

    #a = a.split()
    file1.write(f"{data1['markPrice']} {str(data1['time'])}\n")
    file2.write(f"{data2['markPrice']} {str(data2['time'])}\n")
    file1.flush()
    file2.flush()
    process_data()
    time.sleep(1)

file1.close()
file2.close()

#print(response2.content)

# import pandas as pd
# # Needed to use unverified SSL
# import ssl
# from urllib.request import Request, urlopen
#
# ssl._create_default_https_context = ssl._create_unverified_context
# # For example: BTC/USD data
# url = "https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv"
# request = Request(url)
# request.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0")
# response = urlopen(request)
# df = pd.read_csv(response, delimiter=",", skiprows=[0])
#
#
# print(df)
#

