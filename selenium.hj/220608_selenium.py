

# python3

# >>> from selenium import webdriver
# >>> browser = webdriver.Chrome('./chromedriver')

# >>> browser.get('https://naver.com')


# class name으로 찾을 경우 > find_element_by_class_name
# >>> elem = browser.find_element_by_class_name('link_login')
# >>> elem.click()
# >>> browser.back()
# >>> browser.refresh()
# >>> browser.forward()


# id로 찾을 경우 > find_element_by_id
# >>> elem = browser.find_element_by_id('query')
# >>> from selenium.webdriver.common.keys import Keys
# >>> elem.send_keys("남주혁")
# >>> elem.send_keys(Keys.ENTER)


# #'a' 태그 하나만 가져오기
# >>> elem = browser.find_element_by_tag_name("a")

# # 'a' 태그를 가지고 있는 모든 요소들 가져오기
# >>> elem = browser.find_elements_by_tag_name('a')
# >>> elem
# >>> for e in elem:
#        e.get_attribute("href")
# enter 2번

# click by xpath >>>> 탈출문자 주의!!!
# >>> elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")


# 현재 탭 닫기
# >>> browser.close()

# 모든 브라우저 닫기
# >>> browser.quit()

# python 종료
# >>> exit()


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# url = 'https://naver.com'
# driver.get(url)

browser = webdriver.Chrome('./chromedriver')

# 1.네이버로 이동
browser.get('https://naver.com')

# 2. 네이버 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()


# 3. id, pw 입력
browser.find_element_by_id('id').send_keys("hjjin104")
browser.find_element_by_id('pw').send_keys("1234")

# 4.login 버튼 클릭
browser.find_element_by_id('log.login').click()

time.sleep(3)


# 5. id를 새로 입력
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys("my_id")

# 6.html 정보 출력
print(browser.page_source)

# 7. browser 종료
# browser.close()
browser.quit()
