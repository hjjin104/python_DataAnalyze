from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
# browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights"

browser.get(url)

# delay waiting def


def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath_str)))


# 가는 날 선택
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

# 달력이 하얀 화면으로 딜레이가 걸리기 때문에 time 함수 실행
# time.sleep(2)
wait_until("//b[text() = '27']")

# 이번달 27일 날짜 선택
# browser.find_elements(by=By.LINK_TEXT, value='27')[0].click()
day27 = browser.find_elements(By.XPATH, "//b[text() = '27']")
# print(len(day27))
day27[0].click()

# 이번달 30일 날짜 날짜
day30 = browser.find_elements(By.XPATH, "//b[text() = '30']")
day30[0].click()

# find Arrival button
wait_until('//b[text() ="도착"]')
arrival_airport = browser.find_element(By.XPATH, '//b[text() ="도착"]')

# Click Arrival button
arrival_airport.click()

# delay
wait_until('//button[text() = "국내"]')

# Find & Click Domestic button
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

# find & click jeju airport
wait_until('//i[text()= "제주"]')
find_jeju = browser.find_element(By.XPATH, '//i[text()= "제주"]')
find_jeju.click()


# find & click search
wait_until('//span[text() = "항공권 검색"]')
search_btn = browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]')
search_btn.click()

# Loading Finish before
# Class Name = @
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

# Quit browser
browser.quit()
