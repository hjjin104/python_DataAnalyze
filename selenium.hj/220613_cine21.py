# 라이브러리 선언
from tempfile import TemporaryFile
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

# url address
url = "http://www.cine21.com/rank/boxoffice/domestic"

browser.get(url)

# delay waiting function


def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(By.XPATH, xpath_str))


# 전체 기간 클릭
# wait_until('//a[text() ="1년"]')
total_ranking = browser.find_element(By.XPATH, '//a[text() ="1년"]')
total_ranking.click()

# click search btn
search = browser.find_element(By.XPATH, '//a[text() ="조회"]')
search.click()

time.sleep(2)

# for i in range(0,24):
#     for ii in range(0,10):
#         page = (i*10)+ii+pageNum  print(f"현재페이지는 {page}입니다.")

#         #page num 36 문제 있음
#         if page > 2:
#             print(page)
#             break

#         #Next button click

# 1페이지의 정보
for x in range(0, 24):
    for i in range(0, 10):
        pageNum = x*10+(i+1)
        if pageNum % 10 == 0:
            # Next page button
            next_btn = browser.find_element(
                By.XPATH, '//*[@id="boxoffice_list_content"]/div/a['+str(i+1)+']/span[2]')
            next_btn.click()
            print("10page:", pageNum)
        else:
            next_page = browser.find_element(
                By.XPATH, '//*[@id="boxoffice_list_content"]/div/div/a['+str(pageNum+1)+']')
            next_page.click()
            print("pageNum:",pageNum)
        time.sleep(1)
        # ranking num
        # //*[@id="boxoffice_list_content"]/ul/li[1]/a/span
        # //*[@id="boxoffice_list_content"]/ul/li[2]/a/span
        # //*[@id="boxoffice_list_content"]/ul/li[3]/a/span
        # //*[@id="boxoffice_list_content"]/ul/li[1]/a/span
    for ii in range(0, 2):
        try:
            rank = browser.find_element(
                By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(i*10+ii+1)+']/a/span')
            print(rank.text)
        except:
            print("No value")

    #     # #movie name
    #     try:
    #         movie_name = browser.find_element(
    #             By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(pageNum)+']/a/dpageNum         print(movie_name.text)
    #     except:
    #         print("No value")

    #     # people num
    #     try:
    #         people = browser.find_elements(
    #             By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(pageNum)+']/a/div[2]')
    #         print(people.text)
    #     except:
    #         print("No value")

    #     # third information
    #     try:
    #         thridInfo = browser.find_element(By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(
    #             pageNum)+']/a/div[3]/ul/li[3]').get_attribute("innerText")
    #         print(thridInfo)
    #     except:
    #         print("No value")

    #     # forth Info
    #     try:
    #         forthInfo = browser.find_element(By.XPATH, '//*[@id="boxoffice_list_content"]/ul/li['+str(
    #             pageNum)+']/a/div[3]/ul/li[4]').get_attribute("innerText")
    #         print(forthInfo)
    #     except:
    #         print("No value")
