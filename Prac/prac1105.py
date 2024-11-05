# 예외 처리
try:
    print("나누기 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력했습니다.")
#* ZeroDivisionError: division by zero
except ZeroDivisionError as err:
    print(err) 
