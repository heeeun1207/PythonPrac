kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))
# [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))
# [('사과', '바나나', '오렌지'), ('apple', 'banana', 'orange')]

kor2, eng2 = zip(*mixed)
print(kor2) # ('사과', '바나나', '오렌지')
print(eng2) # ('apple', 'banana', 'orange')
