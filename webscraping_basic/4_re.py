# re : 정규 표현식을 다루는 파이썬 모듈 (Regular Expression)
#* 정규 표현식을 사용하여 특정 형식이 맞는지 검사할 수 있는 예제들 
# 주민등록번호
# 991212-11111
# adcdef-11111 # 잘못된 형태

# 이메일주소 
# abcdef123@gmail.com

# 차량번호 앞2~3자리 
# 11가 1234
# 123가 1234 

# IP주소 
# 192.168.0.1

# 전화번호, URL, 우편번호, 날짜, 시간, 파일 확장자 등...

import re
p = re.compile("ca.e")
def print_match(m):
  
  if m:
    print("m.group():", m.group()) # 일치하는 문자열을 반환
    print("m.string:", m.string) # 입력받은 문자열을 반환 #* .string 변수이므로 괄호없이 씀
    print("m.start():", m.start()) # 일치하는 문자열의 시작 index
    print("m.end():", m.end()) # 일치하는 문자열의 끝 index 
    print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index 
  else:
    print("매칭되지 않음")

# m = p.match("careless") #* 주어진 문자열의 처음부터 일치하는지 확인 > 뒤의 다른값 있어도 매치됨.
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인 
# print_match(m)
# m.group(): care
# m.string: good care
# m.start(): 5
# m.end(): 9 #* 9 이전까지
# m.span(): (5, 9)

# lst = p.findall("careless") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)  # > ['care']

#! 정리 
# 1. p = re.complie("원하는 형태") 
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열 ") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. list = p.findall("비교할 문자열 ") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식 
# . : 하나의 문자를 의미 > (ca.e) : case, cafe
# ^ : 문자열의 시작 > (^de) : desk, destination
# $ : 문자열의 끝 > (se$) : case, base 
