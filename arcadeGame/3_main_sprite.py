# python3.13 -m pip install pygame
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("retro Game") # 게임 이름

# 배경 이미지 불러오기 
background = pygame.image.load("arcadeGame/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("arcadeGame/character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴 
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
#* 가로 중앙위치 기준 오른쪽에 캐릭터가 배치되어있으므로, - 35(캐릭터 가로크기의 절반 옮기기)
character_x_pos = (screen_width / 2) - (character_width /2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 
#* 세로 640 - 70
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래 해당하는는 곳에 위치 

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
  for event in pygame.event.get(): # 어떤 이벤트가 발생했는지 체크
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 
      running = False

  screen.blit(background, (0, 0)) # 배경 그리기

  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update() # 게임화면 다시 그리기!

# pygame 종료
pygame.quit()