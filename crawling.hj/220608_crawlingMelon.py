import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# html에서 동일,반복 구조 변수화
trs = soup.select('#lst50')

# 크롤링한 값들 append할 빈 리스트 생성
rank = []
img = []
title = []
artistA = []
album = []

# 기본 반복 구조에서 필요한 정보 for문 활용하여 추출
for tr in trs:
    a_tag = tr.select_one('td > div')

    if a_tag is not None:
        rank.append(tr.select_one('span.rank').text)
        img.append(tr.select_one('a > img')['src'])
        title.append(tr.select_one(
            'div > div.ellipsis.rank01 > span > a').text)
        artistA.append(tr.select_one(
            'div > div.ellipsis.rank02 > span > a').text)
        album.append(tr.select_one('div > div.ellipsis.rank03 > a').text)

# pandas 활용하여 추출한 데이터 excel 파일로 정리
df = pd.DataFrame(data={"rank": rank, "img": img,
                  "title": title, "artist": artistA, "album": album})
df.to_excel("/Users/jinhyeju/Desktop/coding/dataAnalyze/dataAnalyze_python/Web Crawling/crawling.hj/meloncrawling.xlsx",
            index=False, header=None)
