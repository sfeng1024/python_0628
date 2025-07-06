from http.client import responses

import requests
from bs4 import BeautifulSoup

# responses11 = requests.get("http://books.toscrape.com/")
# print(responses11)
# print(responses11.status_code)
# print(responses11.text)
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"}
# responses11 = requests.get("http://books.toscrape.com/",headers=headers)
# print(responses11.text)
responses11 = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(responses11,"html.parser")
all_prices = soup.findAll("p",attrs={"class":"price_color"})
for price in all_prices:
    print(price.string[2:])
