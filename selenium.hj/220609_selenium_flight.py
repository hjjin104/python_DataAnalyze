from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
# browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights"

browser.get(url)

# 가는 날 선택 클릭
# browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()


# 가는 날 선택
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

# browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button').click()
# # print(type(browser.find_elements_by_link_text('27')))


# 이번달 27일 날짜 선택
# browser.find_elements(by=By.LINK_TEXT, value='27')[0].click()
day27 = browser.find_elements(By.XPATH, "//b[text() = '27']")
# print(len(day27))
day27[0].click()

# 이번달 30일 날짜 날짜
day30 = browser.find_elements(By.XPATH, "//b[text() = '30']")
day30[0].click()

# find Arrival button
arrival_airport = browser.find_element(By.XPATH, '//b[text() ="도착"]')

# Click Arrival button
arrival_airport.click()

# Find & Click Domestic button
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

# find & click jeju airport
find_jeju = browser.find_element(By.XPATH, '//i[text()= "제주"]')
find_jeju.click()


# find & click search
search_btn = browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]')
search_btn.click()

#Loading Finish before
#Class Name = @ 
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

#Quit browser
browser.quit()