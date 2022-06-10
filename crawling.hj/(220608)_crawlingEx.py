from bs4 import BeautifulSoup
# import urllib.request
# reponse = urllib.request.urlopen('http://www.climate.go.kr/home/04_watch/01_3.html').read()

import requests
import time
import pandas as pd
import os
import xlsxwriter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# response = requests.get('http://www.climate.go.kr/home/04_watch/01_3.html', headers=headers)


url_list = ["http://www.climate.go.kr/home/04_watch/01_3.html",
            "http://www.climate.go.kr/home/04_watch/01_3b.html",
            "http://www.climate.go.kr/home/04_watch/01_3c.html",
            "http://www.climate.go.kr/home/04_watch/01_3e.html",
            "http://www.climate.go.kr/home/04_watch/01_3d.html"]
# "http://www.climate.go.kr/home/04_watch/01_3f.php",
# "http://www.climate.go.kr/home/04_watch/01_3g.php"]

response = []
for i in range(0, len(url_list)):
    response.append(requests.get(url_list[i], timeout=1))
# print(response[3].text)

# location
# sub_page > div.watch_tab > div > div > div.box_bottom > p:nth-child(1)

# history
#sub_page > div.watch_tab > div > div > div.box_bottom > p.tit_b

# latitude
# sub_page > div.watch_tab > table > tbody > tr > td:nth-child(1)


soup = []
img = []
location = []
history = []
latitude = []
longtitude = []

# data = []

for i in range(0, len(url_list)):
    soup.append(BeautifulSoup(response[i].text, "html.parser"))
    img.append("https://www.climate.go.kr" + soup[i].find("img")['src'])
    location.append(soup[i].select_one(
        "#sub_page > div.watch_tab > div > div > div.box_bottom > p").text)
    history.append(soup[i].select_one(
        "#sub_page > div.watch_tab > div > div > div.box_bottom > p.tit_b").text)
    latitude.append(soup[i].select_one("td:nth-child(1)").get_text())

    # img = data.append(soup[i].select("img"))
    # location = data.append(soup[i].select_one(
    #     "#sub_page > div.watch_tab > div > div > div.box_bottom > p").text)
    # history = data.append(soup[i].select_one(
    #     "#sub_page > div.watch_tab > div > div > div.box_bottom > p.tit_b").text)
    # latitude = data.append(soup[i].select_one(
    #     "#sub_page > div.watch_tab > table > tbody > tr > td").text)

# print(latitude)
# print(longtitude)

# for x in range(0, len(img)):
#     print(img[x])
# print()
# print(location)
# print()
# print(history)
# print()
# print(latitude)


#
# # for i in range(0, len(img)):
# #     data.append(str(img[i]))


# # # df.to_csv("")


# #현재 경로 검색하기
path_ = os.getcwd()
print(path_)
fileName = "Climate.xlsx"


# df = pd.DataFrame(data={
#     'img': img,
#     "location": location,
#     "history": history,
#     "latitude": latitude
# })
# print(df)

# # df.to_excel(path_, header=True, index=False, engine='xlsxwriter')

# # print(df)
