# balls = [1, 2, 3, 4]
# weapons = [11, 22, 3 , 44]

# for ball_idx, ball_val in enumerate(balls):
#   print("ball :", ball_val)
#   for weapon_idx, weapon_val in enumerate(weapons):
#     print("weapons :", weapon_val)
#     if ball_val == weapon_val: # 충돌 체크
#       print("공과 무기가 충돌")
#       break

# ball : 3
# weapons : 11
# weapons : 22
# weapons : 3
# 공과 무기가 충돌 #* 여기서 break가 안쪽 for문에서만 적용되기 때문 
# ball : 4
# weapons : 11
# weapons : 22
# weapons : 3
# weapons : 44

balls = [1, 2, 3, 4]
weapons = [11, 22, 3 , 44]

for ball_idx, ball_val in enumerate(balls):
  print("ball :", ball_val)
  for weapon_idx, weapon_val in enumerate(weapons):
    print("weapons :", weapon_val)
    if ball_val == weapon_val: # 충돌 체크
      print("공과 무기가 충돌")
      break
    
  else:  # for 에도 else를 적용할 수 있음. 
    continue 
  print("바깥 for 문 break")
  break
# ball : 1
# weapons : 11
# weapons : 22
# weapons : 3
# weapons : 44
# ball : 2
# weapons : 11
# weapons : 22
# weapons : 3
# weapons : 44
# ball : 3
# weapons : 11
# weapons : 22
# weapons : 3
# 공과 무기가 충돌
# 바깥 for 문 break
