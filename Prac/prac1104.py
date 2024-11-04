# # 다양한 출력 포맷
# # 오른쪽 정렬, 총 10자리 공간 확보
# print("{0:>10}".format(500))
# # 양수일 땐 +, 음수일 때 - 표시
# print("{0:>+10}".format(500))
# print("{0:>+10}".format(-500))
# # 왼쪽 정렬, 빈칸 _(밑줄)채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마
# print("{0:,}".format(10000000000))
# # 3자리 콤마 + +-부호 같이 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# # 3자리 콤마 + 부호 + 자리수
# # 빈자리는 ^ 로 표시
# print("{0:^<+30,}".format(10000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

#* 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #* 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동된다.
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#! 활용
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line, end="") #*줄바꿈 없애기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 모든 라인을 가져와서 list 형태로 저장
# for line in lines:
#   print(line.strip())  # .strip()을 사용해 개행 문자 제거


# score_file.close()

#* pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 filed 에 저장
# profile_file.close()
# import pickle
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile에서 불러오기
# print(profile)
# profile_file.close()

# import pickle

# # Person 클래스 정의
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # 피클 파일에서 객체 불러오기
# with open("person.pickle", "rb") as pickle_file:
#     loaded_person = pickle.load(pickle_file)

# # 불러온 객체의 속성 확인
# print(f"이름: {loaded_person.name}, 나이: {loaded_person.age}")

#* with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#   print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
    # study_file.write("파일 만들고 글 쓰기")

# 파일 글 가져오기
# with open("study.txt", "r", encoding="utf8") as study_file:
#   print(study_file.read())

#** 클래스
class Unit:
    """
    C0115: missing-class-docstring" 경고로, 
    클래스 정의에 대한 docstring이 누락됨을 나타냄.
    Python에서 docstring은 클래스, 함수, 모듈 등의 설명을 제공하는 문자열로,
    주로 클래스의 목적이나 사용법을 설명하는 데 사용됨
    """
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
