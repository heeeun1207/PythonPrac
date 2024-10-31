# 주석 
''' 주석 
    여러
    문장 '''
# test
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅎㅎㅎ")
print('ㅎ'*9) 

# boolean 참 / 거짓
print(5 > 10) # False
print(5 < 10) # True
print(False);
print(True);
print(not ( 5 > 10 )) # True

# 변수 
animal = "강아지"
name = "먼지"
age = 2
hobby = "산책"
is_adult = age >= 3 

# +를 콤마(,)로도 대체가능 (단 콤마는 띄어쓰기가 포함된다.)
print("우리집 " + animal + "의 이름은 "  + name + "예요.")
print(name + "는 " + str(age) + "살이며, "+ hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))

station = ["사당", "신도림", "인천공항"]
print(station[0] + "행 열차가 들어오고 있습니다.")

# 연산자
print(2**3) # 2의 3승 

print(2%3) # 2 나머지
print(10%3) # 1
print(10//3) # 몫

print (4 >= 4) # True
print (1+2 == 3) # True

print (1 != 3) # True
print (not ( 1 != 3)) # False

print ((3 > 0) and (3 < 5))
print ((3 > 0) & (3 < 5)) 

print ((3 > 0) and (3 < 5))
print ((3 > 0) | (3 < 5))

print ( 5 > 4 > 3) # True
print ( 5 > 4 > 7) #! False >and and and 

# 간단한 연산
number = 2 + 3 * 4 
print(number) # 14
number += 2
print(number) # 16
number %= 3 
print(number) # 1

# 숫자 처리 함수들
print(abs(-5)) # 5 absolute 절대값 
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 내림

# 랜덤 함수
from random import *

print(random()) # 0.0이상 1.0미만의 임의의 값 생성 
print(random() * 10)  # 0.0이상 10.0미만의 임의의 값 생성 
print(int(random() * 10)) # 정수
print(int(random() * 10) + 1) # 1부터  ~ 10 이하의 임의의 값 지정 

# 로또번호 뽑아보기 
# print(int(random() * 45) + 1) 
# print(int(random() * 45) + 1) 
# print(int(random() * 45) + 1) 
# print(int(random() * 45) + 1) 
# print(int(random() * 45) + 1) 
# print(int(random() * 45) + 1) 
print("로또번호") 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 






