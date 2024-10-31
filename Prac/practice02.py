# 문자열 
sentence = '나는 소녀입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소녀이고, 파이썬은 쉬워요"""
print(sentence3)

# 슬라이싱 = 필요한 정보만 잘라서 사용
jumin ="990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 끝자리를 제외하고 직전값까지 출력됨 99 
# 첫자리와 끝자리는 생략 가능
print("생년월일 : " + jumin[:6]) 
print("뒤 7자리는 : " + jumin[7:])
print("음수값으로 구하기 : " + jumin[-7:])

# 문자열 처리 함수 
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # isupper 지정한 위치값이 대문자인지 확인 # True
print(len(python)) # len 문자 길이
print(python.replace("Python", "Java")) # 값 대체 

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 0 1 -> 두번째 "n" 문자를 찾음
print(index)

print(python.find("Java")) # -1 반환 (찾는 값이 없을 때)
# print(python.index("Java")) #! error 

print(python.count("n")) # 몇 개 있는지 카운팅 

#문자열 포맷
#* 방법 1 
print ("나는 %d살입니다." %20) 
print ("나는 %s을 좋아해요." %"파이썬")  
print ("Apple 은 %c로 시작해요." %"A")  

# print ("나는 %s살입니다." %20) 
# print ("나는 %s을 좋아해요." %"파이썬")  
# print ("Apple 은 %s로 시작해요." %"A")  

print("나는 %s색과 %s색을 좋아해요." %("노란", "보라"))


#* 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("노란", "보라"))
print("나는 {1}색과 {0}색을 좋아해요." .format("노란", "보라"))

#* 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="파란"))

#* 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
#* \" \' : 문장 내에서 따옴표 사용 가능
print("백문이 \n불여일견")
print("나는 '고양이'입니다.")
print("나는 \"고양이\"입니다.")

#* 문장내에서 \ 사용
print("Red Apple\rPine")

#* tab \t
print("Red \tApple")

# 리스트[]
# 지하철 칸별로 10명, 20명, 30명 

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10,20,30]
print(subway.index(10)) # 0

subway.append(40)
print(subway)
subway.insert(1, 15) # insert(삽입할 위치, 값)
print(subway)
print(subway.pop()) # 뒤에서 부터 하나씩 꺼냄
print(subway)

# 정렬 
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
# num_list.clear()
print(num_list) # []

# 다양한 자료형과 함께 사용 가능 
mix_list = ["유재석", 20, True] #['유재석', 20, True]
# print(mix_list)

num_list.extend(mix_list)
print(num_list) # [5, 4, 3, 2, 1, '유재석', 20, True]

