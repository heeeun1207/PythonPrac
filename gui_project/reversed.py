# lst = [1, 2, 3, 4, 5]
# print(lst)
# lst.reverse()
# print(lst)

lst2 = [1, 2, 3, 4, 5]
print("리스트 2 뒤집기 전 : ", lst2)

lst3 = reversed(lst2) # 바뀐 새로운 값이 들어가며, 실제 값에 영향이 미치지 않는다.
print("리스트 2 뒤집은 후 : ",lst2)
print("리스트 3 : ",list(lst3))
# 리스트 2 뒤집기 전 :  [1, 2, 3, 4, 5]
# 리스트 2 뒤집은 후 :  [1, 2, 3, 4, 5]
# 리스트 3 :  [5, 4, 3, 2, 1]
