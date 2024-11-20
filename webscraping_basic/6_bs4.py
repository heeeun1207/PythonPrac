# import requests
# from bs4 import BeautifulSoup

# url = "https://comic.naver.com/index"
# res = requests.get(url)
# res.raise_for_status()  

# soup = BeautifulSoup(res.text, "lxml")

# # 페이지 제목 출력
# title = soup.title.get_text()
# print("페이지 제목:", title)

# # 페이지의 HTML 구조 출력 (전체 HTML을 확인)
# print(soup.prettify())  # 여기서 HTML 구조를 확인

# # "홈" 링크 찾기
# link = soup.find("a", class_="GlobalNavigationBar__link--WMOzG")

# meta_title = soup.find('meta', property='og:title')
# meta_description = soup.find('meta', property='og:description')
# if meta_description:
#     print("메타 설명:", meta_description.get('content'))


############################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()  # 혹은 다른 브라우저 드라이버
driver.get('https://comic.naver.com/index')

# 페이지가 완전히 로드될 때까지 기다리기
driver.implicitly_wait(10)

# 페이지 소스를 가져와서 BeautifulSoup으로 파싱
soup = BeautifulSoup(driver.page_source, 'lxml')

# 이제 soup에서 원하는 요소를 찾을 수 있습니다.
link = soup.find("a", class_="GlobalNavigationBar__link--WMOzG")
if link:
    print("홈 링크:", link.get_text())
    
meta_title = soup.find('meta', property='og:title')
meta_description = soup.find('meta', property='og:description')
if meta_description:
    print("메타 설명:", meta_description.get('content'))
    
driver.quit()  # 브라우저 종료


############################################################

# from selenium import webdriver
# from bs4 import BeautifulSoup

# # 브라우저 드라이버 설정
# driver = webdriver.Chrome()
# driver.get("https://comic.naver.com/index")

# # 페이지 로드 후 HTML 가져오기
# soup = BeautifulSoup(driver.page_source, "lxml")
# element = soup.find("a", attrs={"class": "ContentAuthor__author--CTAAP"})
# if element:
#     print(element.get_text())
# else:
#     print("매칭되는 요소가 없습니다.")

# driver.quit()


############################################################



