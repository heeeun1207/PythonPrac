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