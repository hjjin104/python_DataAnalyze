import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://some.co.kr/media/home', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# for x in range(len(soup)):
#     print(soup)

#Cell title
#mediaList > div.contents_wrap.ranking_list > div.ranking_item_wrap > div > ul > li.detail-open > div.item > div.cell.title
#mediaList > div.contents_wrap.ranking_list > div.ranking_item_wrap > div > ul > li.detail-open > div.item > div.cell.title > a


trs = soup.select(
    '#mediaList > div.contents_wrap.ranking_list > div.ranking_item_wrap > div > ul > li.detail-open > div.item')
print(trs)
# for tr in trs:
#     title = tr.select_one('div.cell.title > a')
#     print(title)

