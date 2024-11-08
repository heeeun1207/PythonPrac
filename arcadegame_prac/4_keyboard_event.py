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

# 이동할 좌표
to_x = 0
to_y = 0 

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
  for event in pygame.event.get(): # 어떤 이벤트가 발생했는지 체크
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 
      running = False

    if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
        to_x -= 5 
      elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
        to_x += 5
      elif event.key == pygame.K_UP: # 캐릭터를 위로
        to_y -= 5
      elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
        to_y += 5 
    
    if event.type == pygame.KEYUP: 
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0 
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
  
          
  character_x_pos += to_x
  character_y_pos += to_y

# 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width

# 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height

  screen.blit(background, (0, 0)) # 배경 그리기

  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update() # 게임화면 다시 그리기!

# pygame 종료
pygame.quit()