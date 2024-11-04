#분기
# weather = "비"
# if 조건: 
# 실행 명령문 

# weather = input("오늘 날씨는 어떄요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요.")

#* if  / elif / else 
# temp = int(input("기온이 어때요? "))    
# if 30 <= temp :
#     print("너무 더워요. 나가지 마세요 ")
# elif 10 <= temp and temp < 30 :
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10 :    # and 와 같은 결과 
#     print("외투를 챙기세요")
# else : 
#     print("너무 추워요. 나가지 마세요")



#* 반복문 
# for waiting_no in [1,2,3,4,5] :
#* randrange()
# for waiting_no in range(5) : # 대기번호 : 0 번부터 시작해서 (5개) 4까지 값을 출력해줌
# for waiting_no in range(1, 6) :
#     print("대기번호 : {0}"  .format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#   print("{0}, 커피가 준비되었습니다." .format(customer))
  
#* while
# customer = "토르"
# index = 3
# while index >= 1 :
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요 " .format(customer, index))
#     index -= 1 
#     if index == 0 :
#       print("커피는 폐기처분되었습니다.")

# customer = "토르"
# person = "Unknown"

# 조건에 만족하면 while문을 탈출 
# while person != customer :
#   print("{0}, 커피가 준비 되었습니다." .format(customer))
#   person = input("이름이 어떻게 되세요? ")


#* continue 와 break 
# absent = [2, 5] # 결석
# no_book = [7] # 책을 안가져옴 
# for student in range (1, 11) : # 1~10
#     if student in absent : 
#       continue
#     elif student in no_book :
#       print("오늘 수업 여기까지. {0}(은)는 교무실로 따라와." .format(student))
#       break
#     print("{0}번, 책을 읽어봐" .format(student))

#* 출석번호 앞에 100을 붙이기로함 1, 2, 3 ... -> 101, 102, 103 ...
# students = [1,2,3,4,5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

#* 길이로 변환 
# students = ["아이언맨", "토르", "아이엠 그루트"] # 길이값은 띄어쓰기 포함 
# students = [len(i) for i in students]
# print(students)

#* 대문자로 변환
# students = ["aaa", "bbb", "vvv"]
# students = [i.upper() for i in students]
# print(students)

#* 함수
# def open_account():
#   print("새로운 계좌가 개설되었습니다.")

# open_account() 

# def deposit(balance, money): # 입금
#     print("입금 완료. 잔액은 {0}원입니다." .format(balance + money))
#     return balance + money 

# def withdraw(balance, money): # 출금
#   if balance >= money :
#     print("출금 완료. 잔액은 {0}원입니다." .format(balance - money))
#     return balance - money
#   else:
#     print("출금 에러. 잔액은 {0}원입니다." .format(balance))
#     return balance
  
# def withdraw_night(balance, money): 
#   commission = 100 # 수수료
#   #! 여러개 값 반환
#   return commission, balance - money - commission
  
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

#* 기본값 
# def profile(name, age, main_lang):
#   print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("강동원", 25, "자바")

# 기본값 설정 
# def profile(name, age=17, main_lang="파이썬"):
#   print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" .format(name, age, main_lang))
# profile("유재석")
# profile("강동원")

#* 키워드 값을 이용한 함수 호출
# def profile(name, age, main_lang):
#   print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", name="강동원", age=20) #* 순서가 알아서 정렬됨. 
# 유재석 20 파이썬
# 강동원 20 자바

#* 가변 인자
# def profile(name, age, lang1, lang2 , lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t" .format(name, age), end =" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t 나이 : {1}\t" .format(name, age), end =" ")
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#") 

#* 지역변수, 전역변수
gun = 10 

# def checkpoint(soldiers): # 경계근무
#   # gun = 20
#   global gun  #* 전역 변수 사용 
#   gun = gun - soldiers
#   print("[함수 내] 남은 총 : {0}". format(gun))
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은총 : {0}".format(gun)) 

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}". format(gun))
#     return gun 

# gun = checkpoint_ret(gun, 2)
# print("남은총 : {0}".format(gun))

#* 표준 입출력
# print("Python","Java", "JavaScript", sep=" & ")
# print("Python","Java", "JavaScript", end=" ")   #* 줄바꿈 없이 연속 출력 가능 
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #* 표준출력
# print("Python", "Java", file=sys.stderr) #* 표준에러

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(5), str(score).rjust(4), sep=":")

# 은행 대기순번표
# for num in range(1, 4):
#     print("대기번호 : " + str(num).zfill(3)) # 대기번호 : 001

answer = input("아무값이나 입력 : ")
# print(type(answer)) #! 사용자 입력을 통해서 값을 받으면 항상 문자열 형태이다. <class 'str'>
print("입력한 값은 " + answer + "입니다.")
