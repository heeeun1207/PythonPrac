# 최근 코딩 스터디 모임을 새로 만들었다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 정했다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외 

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. 
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다. ")


#02 
# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 규칙 1 : http:// 부분은 제외 
# 규칙 2 : 처음 만나는 점(.) 이후를 제외 
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성해라 
url = "http://naver.com"
my_str = url.replace("http://", "")
#print(my_str)
my_str = my_str[:my_str.index(".")]
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))


#03 
# 댓글 이벤트를 진행한다.
# 댓글 작성자 중에서 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# 활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성 
print(type(users)) # <class 'range'> 
# 타입 변환 시키기 
users = list(users)
print(type(users)) # <class 'list'>

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은  커피
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))