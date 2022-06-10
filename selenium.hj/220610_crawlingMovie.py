import time

from bs4 import BeautifulSoup
import pandas as pd
import requests

# 라이브러리 선언
from selenium import webdriver
from selenium.webdriver.common.by import By

# 드라이버 위치 설정
driver_loc = "./chromedriver"

# 드라이버 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("window-size=2560x1600")

# 웹 드라이버 정의
driver = webdriver.Chrome(driver_loc, options=options)
# 웹페이지 파싱 될때까지 최대 3초 기다림
driver.implicitly_wait(3)


# URL 정의
sparkUrl = 'http://www.cine21.com/rank/boxoffice/domestic'

# URL 이동
driver.implicitly_wait(3)
driver.get(sparkUrl)


df = pd.DataFrame(columns=['제목', '관객수', '이미지'])
driver.find_element(By.XPATH, '//*[@id="data_period"]/a[6]').click()
time.sleep(2)

# for pages in range(0, 25):  # 총 페이지 233 페이지, 240 페이지 까지 가는 걸로

# for i in range(0, 24):
#     if i == 23:
#         for ii in range(0, 3):
#             driver.find_element(
#                 By.XPATH, '//*[@id="boxoffice_list_content"]/div/div/a['+str(i*10+ii+1)+']').click()
#     elif i < 23:
#         for ii in range(0, 10):
# # 나온 값이 나누기 10을 했을 때 나머지가 0일 경우 화살표 클릭
#             driver.find_element(
#                 By.XPATH, '//*[@id="boxoffice_list_content"]/div/div/a['+str(i*10+ii+1)+']').click()

for pages in range(0, 24):
    while True:
        for page in range(pages*10+1, pages*10+11):
            if page < 234:
                driver.find_element(
                    By.XPATH, '//*[@id="boxoffice_list_content"]/div/div/a['+str(page)+']').click()
                time.sleep(1)
                if page % 10 == 0:
                    page_buttons = driver.find_element_by_class_name(
                        'btn_next')
                    page_buttons.click()
                continue
            if page == 234:
                break




# 현재 페이지 소스 가져오기
html = driver.page_source

title_list = []
img_list = []
people_list = []

for i in range(0, 5):
    try:
        title_list.append(driver.find_element(
            By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(i+1)+']/a/div[1]'))

    except:
        title_list.append('값없음')

    try:
        img_list.append(driver.find_element(
            By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(i+1)+']/a/img'))

    except:
        title_list.append('값없음')

    try:
        people_list.append(driver.find_element(
            By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(i+1)+']/a/div[2]'))
    except:
        title_list.append('값없음')

        df2 = pd.DataFrame()
        df2.insert(0, '제목', title_list)
        df2.insert(1, '관객수', people_list)
        df2.insert(2, '이미지', img_list)

        df = pd.concat([df, df2])

# 확인
print(df)
print(df.columns)

# Create File
df.to_excel('/Users/jinhyeju/Desktop/coding/dataAnalyze/dataAnalyze_python/Web Crawling/cine21.xlsx', index=False,
            header=['제목', '관객수', '이미지'], engine="xlsxwriter")


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(
#     'http://www.cine21.com/rank/boxoffice/domestic', headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')

# # 영화 한 단위
# # boxoffice_list_content > ul > li:nth-child(1)
# # boxoffice_list_content > ul > li:nth-child(2)

# # 영화에서 랭킹
# # boxoffice_list_content > ul > li:nth-child(2) > a > span

# # 영화에서 제목
# # boxoffice_list_content > ul > li:nth-child(1) > a > div.mov_name
# # boxoffice_list_content > ul > li:nth-child(2) > a > div.mov_name

# # 이미지
# # boxoffice_list_content > ul > li:nth-child(1) > a > img

# trs = soup.select('#boxoffice_list_content > ul > li > a')

# for tr in trs:
#     rank = tr.select_one('span.grade num1')
#     title = tr.select_one('div.mov_name').text
#     img = tr.select('img')
#     print(img)
