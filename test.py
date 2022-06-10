# for i in range(2, 10):
#     for x in range(1, 10):
#         print(i*x, end=" ")
#     print()

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a)
