# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1
import csv 
import requests
from bs4 import BeautifulSoup

url ="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=" 

filename = "시가총액 1-200.csv"
# utf-8-sig
# 주로 Windows 환경에서 MS Excel과 같은 프로그램이 CSV 파일을 올바르게 인식하도록 하기 위해 사용
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

for page in range(1, 5):
  res = requests.get(url + str(page))
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")
  
  data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
  for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1: # 의미 없는 데이터 skip 
      continue
    data = [column.get_text().strip() for column in columns]
    # print(data)
    writer.writerow(data)
    
