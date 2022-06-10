import time

from bs4 import BeautifulSoup
import pandas as pd
import requests

# 라이브러리 선언
from selenium import webdriver
from selenium.webdriver.common.by import By

# 드라이버 위치 설정
driver_loc = "C:\\Users\\a\\Desktop\\chromedriver.exe"

# 드라이버 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("window-size=2560x1600")

# 헤드리스 설정 시 리눅스 같이 웹화면 없는경우에도 웹페이지 실행가능함
# options.add_argument('headless’)
# options.add_argument("disable-gpu")
# 웹 드라이버 정의
driver = webdriver.Chrome(driver_loc, options=options)
# 웹페이지 파싱 될때까지 최대 3초 기다림
driver.implicitly_wait(3)


# URL 정의
sparkUrl = 'http://www.cine21.com/rank/boxoffice/domestic'

# URL 이동
driver.implicitly_wait(3)
driver.get(sparkUrl)

# 전체기간클릭처리
일년기간버튼 = '#data_period a:nth-child(12)'
driver.find_element_by_xpath(일년기간버튼).click()
time.sleep(3)    # 3초간 기다림


df = pd.DataFrame(columns=['제목', '관객수', '누적관객수', '개봉일'])
# 1~ 233
# 10개 단위
for pages in range(0, 20): 
    for page in range(pages*5 + 1, pages*5 + 6):
        if page <90:
            driver.find_element(By.LINK_TEXT, str(page)).click()
        time.sleep(3)

        print("pages : ", pages)
        print("page : ", page)

# for pages in range (0, 20):
#     for page in range(pages*5 + 2, pages*5 + 6):
        # 이후 뷰티플숩으로 소스가저오기

        # 현재 페이지 소스 가져오기
        html = driver.page_source

        # import bs4
        # # BeautifulSoup로 페이지 소스 파싱
        # bs = bs4.BeautifulSoup(html, "html.parser", from_encoding='utf-8')

        # # 뷰티플숩과 셀레니움 병용
        # # find_element 와 elements 둘다 있음
        # title = bs.select('.ellipsis')
        # contents_image = bs.select('#content img')

        # title_list = []
        # contents_image_list = []

        # for i in range(0, len(title)):
        #     title_list.append(title[i].string.strip())
        #     contents_image_list.append(contents_image[i]['src'])

        제목 = []
        관객수 = []
        누적관객수 = []
        개봉일 = []

        for i in range(0, 20):
            try:
                제목.append(driver.find_element(By.XPATH, 
                    '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[2]/div[1]/h5').text)
            except:
                제목.append('값없음')
            try:
                관객수.append(driver.find_element(By.XPATH, 
                    '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[1]/img').get_attribute('src'))
            except:
                관객수.append('값없음')
            try:
                누적관객수.append(driver.find_element(By.XPATH, 
                    '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[2]/div[2]/div[1]').text)
            except:
                누적관객수.append('값없음')
            try:
                개봉일.append(driver.find_element(By.XPATH, 
                    '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[2]/div[3]').text)
            except:
                개봉일.append('값없음')
            
        df2=pd.DataFrame()
        df2.insert(0, '제목', 제목)
        df2.insert(1, '관객수', 관객수)
        df2.insert(2, '누적관객수', 누적관객수)
        df2.insert(3, '개봉일', 개봉일)

        df = pd.concat([df, df2])

        if page%10 == 0:
            # driver.find_element(By.LINK_TEXT, '다음').click()
            driver.find_element(By.XPATH, '//*[@id="boxoffice_list_content"]/div/a[2]/span[2]')
        if page == 230:
            break

# 확인
print(df)
print(df.columns)

df.to_excel("C:\\Users\\a\\Desktop\\onoffmix.xlsx", index=False,
            header=['타이틀', '이미지', '분류', '테그', '기간', '장소', '가능', '데드라인'])