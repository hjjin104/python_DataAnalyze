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

# 헤드리스 설정 시 리눅스 같이 웹화면 없는경우에도 웹페이지 실행가능함
# options.add_argument('headless’)
# options.add_argument("disable-gpu")
# 웹 드라이버 정의
driver = webdriver.Chrome(driver_loc, options=options)
# 웹페이지 파싱 될때까지 최대 3초 기다림
driver.implicitly_wait(3)


# URL 정의
sparkUrl = 'https://www.onoffmix.com/event/main/'

# URL 이동
driver.implicitly_wait(3)
driver.get(sparkUrl)

# 리스트형으로 보기바꿈
quizBtnXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "btn_list", " " ))]'
driver.find_element_by_xpath(quizBtnXpath).click()
time.sleep(3)    # 3초간 기다림


df = pd.DataFrame(columns=['타이틀', '이미지', '분류', '테그', '기간', '장소', '가능', '데드라인'])


for pages in range(0, 2):
    for page in range(pages*5 + 1, pages*5 + 6):
        if page < 90:
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

        title_list = []
        contents_image_list = []
        분류_list = []
        tags_list = []
        기간_list = []
        장소_list = []
        가능_list = []
        데드라인_list = []

        for i in range(0, 5):
            try:
                title_list.append(driver.find_element(By.XPATH,
                                                      '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[2]/div[1]/h5').text)
            except:
                title_list.append('값없음')
            try:
                contents_image_list.append(driver.find_element(By.XPATH,
                                                               '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[1]/img').get_attribute('src'))
            except:
                contents_image_list.append('값없음')
            try:
                분류_list.append(driver.find_element(By.XPATH,
                                                   '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[2]/div[2]/div[1]').text)
            except:
                분류_list.append('값없음')
            try:
                tags_list.append(driver.find_element(By.XPATH,
                                                     '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[2]/div[3]').text)
            except:
                tags_list.append('값없음')
            try:
                기간_list.append(driver.find_element(By.XPATH,
                                                   '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[3]/div/span[1]').text)
            except:
                기간_list.append('값없음')
            try:
                장소_list.append(driver.find_element(By.XPATH,
                                                   '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[3]/div/span[2]').text)
            except:
                장소_list.append('값없음')

            if page < 50:
                try:
                    가능_list.append(driver.find_element(By.XPATH,
                                                       '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[4]/div/span[1]').text)
                except:
                    가능_list.append('값없음')
                try:
                    데드라인_list.append(driver.find_element(By.XPATH,
                                                         '//*[@id="content"]/div/section[2]/ul/li[' + str(i+1) + ']/article[1]/a/div[4]/div/span[2]').text)
                except:
                    데드라인_list.append('값없음')
            if page >= 50:
                가능_list.append("마감")
                데드라인_list.append('값없음')

        df2 = pd.DataFrame()
        df2.insert(0, '타이틀', title_list)
        df2.insert(1, '이미지', contents_image_list)
        df2.insert(2, '분류', 분류_list)
        df2.insert(3, '테그', tags_list)
        df2.insert(4, '기간', 기간_list)
        df2.insert(5, '장소', 장소_list)
        df2.insert(6, '가능', 가능_list)
        df2.insert(7, '데드라인', 데드라인_list)

        df = pd.concat([df, df2])

        if page % 5 == 0:
            driver.find_element(By.LINK_TEXT, '다음').click()
        if page == 90:
            break

# 확인
print(df)
print(df.columns)

df.to_excel("/Users/jinhyeju/Desktop/coding/dataAnalyze/dataAnalyze_python/Web Crawling/test.xlsx", index=False,
            header=['타이틀', '이미지', '분류', '테그', '기간', '장소', '가능', '데드라인'], engine="xlsxwriter")
