from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup
import urllib
import time
import os
import pandas as pd
import sys

from sqlalchemy import create_engine
engine = create_engine(
    'mysql+mysqldb://expert01:expert01!pass@192.168.0.35:3306/expert01')
print(engine.execute("desc test01table").fetchone())  # test 테이블의 schema를 출력

time.sleep(2222)


Session = sessionmaker(engine)  # Engine에 종속적인 Session을 정의하고
session = Session()  # Session 객체를 만든다
Base = declarative_base()

# str을 class 로 변환해주는 함수


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


절대경로 = os.getcwd()
파일명 = "기상청.xlsx"
파일이저장되는경로 = os.path.join(절대경로, 파일명)

url_list = []
url_list = [
    "http://www.climate.go.kr/home/04_watch/01_3.html",
    "http://www.climate.go.kr/home/04_watch/01_3b.html",
    "http://www.climate.go.kr/home/04_watch/01_3c.html",
    "http://www.climate.go.kr/home/04_watch/01_3e.html",
    "http://www.climate.go.kr/home/04_watch/01_3d.html",
    "http://www.climate.go.kr/home/04_watch/01_3f.php",
    "http://www.climate.go.kr/home/04_watch/01_3g.php",
]


response = []
for i in range(0, len(url_list)):
    response.append(requests.get(url_list[i], timeout=1000))

for i in range(0, len(url_list)):
    # globals 가변 변수를 만드는 함수
    globals()["soup{}".format(i)] = BeautifulSoup(
        response[i].text, "html.parser")

img = []
소재지 = []
감시연혁 = []
위경도 = []
감시요소 = []
위탁지정일 = []

for i in range(0, len(url_list)):
    img.append("http://www.climate.go.kr" +
               str(str_to_class(f"soup{i}").findAll("img")[4]['src']))
    소재지.append(str(str_to_class(f"soup{i}").select(
        "#sub_page p:nth-child(1)")[0].get_text()))
    감시연혁.append(str(str_to_class(f"soup{i}").select(".tit_b")[0].get_text()))
    위경도.append(str(str_to_class(f"soup{i}").select(
        "td:nth-child(1)")[0].get_text()))
    감시요소.append(str(str_to_class(f"soup{i}").select(".box_le")[0].get_text()))
    위탁지정일.append(str(str_to_class(f"soup{i}").select(
        ".box_le+ td")[0].get_text()))

data = {
    "img": img,
    "소재지": 소재지,
    "감시연혁": 감시연혁,
    "위경도": 위경도,
    "감시요소": 감시요소,
    "위탁지정일": 위탁지정일,
}

df = pd.DataFrame(data=data)  # data는 위의 딕셔너리 data를 입력

df.to_excel(파일이저장되는경로, sheet_name="기상청1", header=True,
            index=False, engine="xlsxwriter")

# df.to_csv(파일이저장되는경로)
# 또는 DB에 담을 수 있음

# ~~~~~~~~~~~~~~~~~~~~~~~~~~
