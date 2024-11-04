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
from random import *
# 일반 유닛 
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed =speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 공격 유닛
class AttackUnit(Unit): # Unit 을 상속 받음 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
        
        # 스팀팩 : 일정 시간 동안 공격 속도를 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크 클래스
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 이동은 불가능
    seize_developed = False # 시즈모드 개발여부    

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return 
        
        # 현재 시즈모드가 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환 합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True        
        # 현재 시즈모드 일 때 -> 시즈모드 해제
        else : 
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False  
        
# 날 수 있는 기능을 가진 클래스 
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 
class FlyableAttackUnit(AttackUnit, Flyable): #! 다중 상속 : AttackUnit, Flyable 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 처리
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): #! 오버라이딩 : move() 재정의
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태))
        
    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 설정
            print("{0} 클로킹 모드 설정.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") 
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
    
# 게임 시작
game_start()

# 유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 이동시키기
for unit in attack_units: 
    unit.move("1시")

# tank 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발 완료됨.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드 , 레이스 : 클로킹 )
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격 
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5~20)

# 게임 종료
game_over()