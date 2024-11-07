# from travel import *
# import inspect 
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

#* pip install 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

#* 내장함수 
#* input : 사용자 입력을 받는 함수 
# language = input("무슨 언어를 좋아하세요?")
# print("{}은 아주 좋죠 !".format(language))

#* dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 
# print(dir())
# import random #* 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

#* glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# # 경로 지정 확인: glob.glob("*.py")는 현재 디렉토리의 .py 파일만 찾기 때문에, 
# # 다른 폴더에 .py 파일이 있는 경우 해당 경로를 지정해야 한다. 
# print(glob.glob("Game/*.py"))

#* os : 운영체제에서 제공하는 기본 기능 
# import os 
# print(os.getcwd()) # 현재 디렉토리 표시

# folder = "sample_dir"
# if os.path.exists(folder):
#   print("이미 존재하는 폴더입니다.")
#   os.rmdir(folder)
#   print(folder, "폴더를 삭제하였습니다.")
# else:
#   os.makedirs(folder) # 폴더 생성
#   print(folder, "폴더를 생성하였습니다.")

# print(os.listdir("Game"))

#* time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

#* timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100일에 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후
