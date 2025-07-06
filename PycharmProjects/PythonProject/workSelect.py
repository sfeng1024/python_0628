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
responses11 = requests.get("https://www.shixiseng.com").text
responses12 = requests.get("https://www.shixiseng.com")
print(responses12.status_code)
soup = BeautifulSoup(responses11,"html.parser")
job_tags = soup.find_all('a', class_='text')
titles = soup.find_all('a', class_='title')
salaries = soup.find_all('span', class_='salary')

# print(responses11)
# all_prices = soup.findAll("p",attrs={"class":"price_color"})
# for price in job_tags:
#     print(price.string[2:])
for i, tag in enumerate(job_tags[:5], start=1):
    print(f"{i}. 岗位名称：{tag.text.strip()}")

# 提取前 5 个岗位和薪资
for i in range(min(5, len(titles), len(salaries))):
    title = titles[i].get_text(strip=True)
    salary = salaries[i].get_text(strip=True)
    print(f"{i+1}. {title}：{salary}")