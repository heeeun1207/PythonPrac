# 예외 처리
# try:
#     print("나누기 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요.")))
#     nums.append(int(input("두 번째 숫자를 입력하세요.")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다.")
# #* ZeroDivisionError: division by zero
# except ZeroDivisionError as err:
#     print(err) 
# except Exception as err:
#     print("알 수없는 에러 발생!")
#     print(err)

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print ("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError :
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

#* 사용자 정의 예외 처리 
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print ("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생했습니다. 한 자리 숫자만 입력하시오.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

#*모듈
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

#* 패키지
# import travel.thailand #! 마지막은 모듈이나 패키지만 올수있다.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #! 모듈 패키지 클래스함수 모두 가져올 수 있음.
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import * #! __init__.py 에 추가 
trip_to = thailand.ThailandPackage()
trip_to.detail()

