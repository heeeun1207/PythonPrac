# 사전
cabinet = {3 : "유재석", 100 : "강동원"} # key : value
print(cabinet[3]) # 유재석
print(cabinet[100]) # 강동원

print(cabinet.get(3)) # 유재석

#! 차이 
# print(cabinet[5]) #! KeyError
print(cabinet.get(5)) # None
#* 기본값을 적용하고 싶다면 
print(cabinet.get(5, "기본값"))

print (3 in cabinet) # 해당값이 존재하면 True / 아니면 False 


# String
cabinet2 = {"A-3" : "고양이", "B-100" : "강아지"}
print(cabinet2["A-3"])

# 추가
cabinet2["A-3"] = "양"
cabinet2["C-20"] = "돼지"
print(cabinet2)

# 삭제
del cabinet2["A-3"]
print(cabinet2)

# 출력 방법 
print(cabinet2.keys()) # key만 -> dict_keys(['B-100', 'C-20'])
print(cabinet2.values()) # dict_values(['강아지', '돼지'])
print(cabinet2.items()) # dict_items([('B-100', '강아지'), ('C-20', '돼지')])

# 튜플 (리스트와 다르게 내용 변경이나 추가는 할 수 없지만, 속도가 빠르다.)
menu = ("돈까스", "치즈돈까스")
print(menu[0])
# menu.add("생선까스") #! AttributeError: 'tuple' object has no attribute 'add'


# 변수 할당 방법 
# name = "김철수"
# age = 20
# hobby = "코딩"

(name, age, hobby) = ("김철수", 20, "코딩")
print(name,age,hobby)

# 집합 (set) 
#* 중복이 안됨, 순서가 없음. 
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"홍길동", "김철수", "김수지"}
python = set(["홍길동", "강동원"])

# 교집합 
print(java & python) # {'홍길동'} 
print(java.intersection(python))

# 합집합 
print(java | python)
print(java.union(python))

# 차집합 (java만 할 수 있는 개발자)
print(java - python)
print(java.difference(python))

# 추가 add
python.add("김수지")
print(python)

# 삭제 remove
java.remove("김철수")
print(java)

#* 자료 구조의 변경
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu)) # <class 'set'>

menu = list(menu) 
print(menu, type(menu)) # <class 'list'>
