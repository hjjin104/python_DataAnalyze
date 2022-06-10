from matplotlib import artist
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.cine21.com/rank/boxoffice/domestic', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#boxoffice_list_content > ul > li:nth-child(1)

trs = 