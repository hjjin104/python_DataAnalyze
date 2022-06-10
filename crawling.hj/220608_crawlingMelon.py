
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# lst50
# lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
# lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
# lst50 > td:nth-child(7) > div > div > div > a
# lst50 > td:nth-child(7) > div > div > div
# lst50 > td:nth-child(2) > div > span.rank
# lst50 > td:nth-child(4) > div > a > img

trs = soup.select('#lst50 > td > div')

for tr in trs:
    rank = tr.select_one('span.rank').text
    img = tr.select_one(' a > img')['src']
    title = tr.select_one(
        'div > div.ellipsis.rank01 > span > a').text
    artistA = tr.select_one(
        'div > div.ellipsis.rank02 > span > a').text
    album = tr.select_one('div > div.ellipsis.rank03 > a').text
    print(rank, img, title, artistA, album)
