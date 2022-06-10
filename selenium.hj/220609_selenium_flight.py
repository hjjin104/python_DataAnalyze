from selenium import webdriver
browser = webdriver.Chrome('./chromedriver')
# browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights"

browser.get(url)

#가는 날 선택 클릭 
browser.find_element_by_class_name('modal_modal__1rTeN').click()
#이번달 27일, 28일 선택
# browser.find_elements_by_name("sc-evZas dDVwEk num")[0].click() #이번달 27 선택
# browser.find_elements_by_link_text("sc-evZas dDVwEk num")[27].click() #이번달 27 선택
