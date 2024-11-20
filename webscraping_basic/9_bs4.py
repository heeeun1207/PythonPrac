# GET 방식 
#* ?변수 = 값 & 변수 = 값 & 변수 = 값 ...  
# "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="

# import requests
# from bs4 import BeautifulSoup
# url = "https://www.coupang.com/"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"

# 헤더에 User-Agent 추가 (브라우저에서 보내는 요청처럼 보이게)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# 요청 보내기
res = requests.get(url, headers=headers, timeout=10)  # 10초로 타임아웃 설정
res.raise_for_status()  # 요청이 실패하면 오류 발생

soup = BeautifulSoup(res.text, "lxml")

print(soup.prettify())  # HTML 구조를 예쁘게 출력하여 확인


