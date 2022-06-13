from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
# browser.maximize_window()  # 창 최대화

url = "https://wwws.airfrance.co.kr/"

browser.get(url)

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath_str)))


#cookie 
# wait_until('//button[text() ="수락"]')
time.sleep(3)
cookie = browser.find_element(By.XPATH,'//button[text() ="거절"]')
cookie.click()

# login_btn
# wait_until('//span[text() = "로그인"]')
# login_btn = browser.find_element(By.XPATH, '//span[text() = "로그인"]')
# login_btn = browser.find_element_by_class_name("mat-ripple mat-button-ripple mat-button-ripple-round")
login_btn = browser.find_element(By.XPATH,'//span[@class="bwc-o-body-variant bwc-logo-header__label-login"]')
login_btn.click()