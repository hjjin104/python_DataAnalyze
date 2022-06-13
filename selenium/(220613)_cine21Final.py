# 라이브러리 선언
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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
sparkUrl = "http://www.cine21.com/rank/boxoffice/domestic"

# URL 이동
driver.implicitly_wait(3)
driver.get(sparkUrl)

# 전체기간클릭처리
일년기간버튼 = '//*[@id="data_period"]/a[6]'
driver.find_element_by_xpath(일년기간버튼).click()

# 조회버튼클릭처리
조회버튼 = '//*[contains(concat( " ", @class, " " ), concat( " ", "btn_red_s", " " ))]'
driver.find_element_by_xpath(조회버튼).click()

# data = {"제목": "1", "관객수": "ㅁ", "누적관객수": "1", "개봉일": "ㅁ"}
# df = pd.DataFrame(data={}, columns=["제목", "관객수", "누적관객수", "개봉일"])

# 가져올 내용
img = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/img
제목 = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[1]
관객수 = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[2]
마우스호버시나오는정보1 = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[1]/span
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[1]/text()
마우스호버시나오는정보2 = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[2]/span
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[2]/text()
마우스호버시나오는정보3 = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[3]/span
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[3]/text()
마우스호버시나오는정보4 = []
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[4]/span
# //*[@id="boxoffice_list_content"]/ul/li[1]/a/div[3]/ul/li[4]/text()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


for i in range(0, 24):  # 233개의 페이지 10개씩, 20개의 영화
    for ii in range(0, 10):
        현재페이지숫자 = (i * 10) + ii + 1
        print(f"현재페이지는 {현재페이지숫자} 입니다")

        # 페이지 36 문제있음 (씨네21자체문제)
        if 현재페이지숫자 > 2:
            # if 현재페이지숫자 > 35:
            break

        if 현재페이지숫자 % 10 != 0:
            페이지버튼숫자의XPATH = (
                '//*[@id="boxoffice_list_content"]/div/div/a[' +
                str(현재페이지숫자 % 10) + "]"
            )
        else:
            페이지버튼숫자의XPATH = (
                '//*[@id="boxoffice_list_content"]/div/div/a['
                + str((현재페이지숫자 % 10) + 10)
                + "]"
            )
        print(f"페이지버튼숫자의XPATH는 {페이지버튼숫자의XPATH}입니다.")
        # 링크텍스트로 클릭
        driver.find_element_by_xpath(페이지버튼숫자의XPATH).click()
        # 클릭후 조금기다림
        time.sleep(2)

        # 현페이지의 html 담음
        html = driver.page_source
        # 페이지당 20개의 영화 (정보추출)
        for iii in range(0, 20):
            try:
                img.append(
                    driver.find_element_by_xpath(
                        '//*[@id="boxoffice_list_content"]/ul/li['
                        + str(iii + 1)
                        + "]/a/img"
                    ).get_attribute("src")
                )
            except:
                img.append("값없음")

            try:
                제목.append(
                    driver.find_element_by_xpath(
                        '//*[@id="boxoffice_list_content"]/ul/li['
                        + str(iii + 1)
                        + "]/a/div[1]",
                    ).text
                )
            except:
                제목.append("값없음")

            try:
                관객수.append(
                    driver.find_element_by_xpath(
                        '//*[contains(concat( " ", @class, " " ), concat( " ", "boxoffice_li", " " )) and (((count(preceding-sibling::*) + 1) = '
                        + str(iii + 1)
                        + ') and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "people_num", " " ))]',
                    ).text
                )
            except:
                관객수.append("값없음")

            try:
                마우스호버시나오는정보1.append(
                    driver.find_element_by_xpath(
                        '//*[@id="boxoffice_list_content"]/ul/li['
                        + str(iii + 1)
                        + "]/a/div[3]/ul/li[1]",
                    ).get_attribute("innerText")
                )
            except:
                마우스호버시나오는정보1.append("값없음")

            try:
                마우스호버시나오는정보1.append(
                    driver.find_element_by_xpath(
                        '//*[@id="boxoffice_list_content"]/ul/li['
                        + str(iii + 1)
                        + "]/a/div[3]/ul/li[2]",
                    ).get_attribute("innerText")
                )
            except:
                마우스호버시나오는정보2.append("값없음")

            try:
                마우스호버시나오는정보3.append(
                    driver.find_element_by_xpath(
                        '//*[@id="boxoffice_list_content"]/ul/li['
                        + str(iii + 1)
                        + "]/a/div[3]/ul/li[3]",
                    ).get_attribute("innerText")
                )
            except:
                마우스호버시나오는정보3.append("값없음")

            try:
                마우스호버시나오는정보4.append(
                    driver.find_element_by_xpath(
                        '//*[@id="boxoffice_list_content"]/ul/li['
                        + str(iii + 1)
                        + "]/a/div[3]/ul/li[4]",
                    ).get_attribute("innerText")
                )
            except:
                마우스호버시나오는정보4.append("값없음")

        print(f"{현재페이지숫자}페이지 작업이 완료 되었습니다. 다음페이지 {현재페이지숫자+1}로 넘어가겠습니다.")

        # 현재페이지숫자 나누기 10을 했을때 나머지가 0일경우 다음페이지는 화살표 클릭
        # 아닐경우 다음페이지 숫자클릭
        if 현재페이지숫자 % 10 == 0:
            print(f"현재페이지숫자10의배수여부 : {현재페이지숫자%10 == 0}")
            if i == 0:
                화살표한개버튼 = '//*[@id="boxoffice_list_content"]/div/a[2]/span[2]'
            else:
                화살표한개버튼 = '//*[@id="boxoffice_list_content"]/div/a[3]/span[2]'
            driver.find_element_by_xpath(화살표한개버튼).click()
            time.sleep(2)
            print(f"화살표버튼눌러 이동했습니다.")
        else:
            # 다음페이지이동
            다음페이지숫자 = (현재페이지숫자 % 10) + 1
            다음페이지버튼숫자XPATH = (
                '//*[@id="boxoffice_list_content"]/div/div/a[' +
                str(다음페이지숫자) + "]"
            )
            driver.find_element_by_xpath(다음페이지버튼숫자XPATH).click()
            time.sleep(2)
            print(f"페이지 {현재페이지숫자+1}으로 이동했습니다.")

# 브라우저제어 종료
driver.quit()

items = [
    img,
    제목,
    관객수,
    마우스호버시나오는정보1,
    마우스호버시나오는정보2,
    마우스호버시나오는정보3,
    마우스호버시나오는정보4,
]

for item in items:
    print(f"{len(item)}")
    print(f"{item}")


# time.sleep(88888)

# 후처리

df = pd.DataFrame(
    data={
        "img": img,
        "제목": 제목,
        "관객수": 관객수,
        # 갯수문제로 병합제외
        # "마우스호버시나오는정보1": 마우스호버시나오는정보1,
        # "마우스호버시나오는정보2": 마우스호버시나오는정보2,
        # "마우스호버시나오는정보3": 마우스호버시나오는정보3,
        # "마우스호버시나오는정보4": 마우스호버시나오는정보4,
    },
)
print(df)

df.to_excel(
    "C:\\Users\\a\\Desktop\\씨네21.xlsx",
    index=False,
    header=[
        "이미지주소",
        "영화제목",
        "관객수",
        # 병합제외
        # "마우스호버시나오는정보1",
        # "마우스호버시나오는정보2",
        # "마우스호버시나오는정보3",
        # "마우스호버시나오는정보4",
    ],
)

# 멀티프로세싱
# 주소체계의 나누어지는 API등에 적용하면
# 완료까지의 시간을 아낄수 있다
# 셀레니움 파서를 다시 뷰티플숩으로 옮겨서 이용하면
# 속도를 개선할수 있다
# https://medium.com/@winston.smith.spb/python-selenium-speed-scraping-45bda525e42

# 포멧터 작동시 문자열 변경이 일어날수 있음
# XPATH 문자열을 넣어두고 비교해볼것
