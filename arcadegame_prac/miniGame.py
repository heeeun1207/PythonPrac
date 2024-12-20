#* 하늘에서 떨어지는 똥 피하기 게임을 만드시오.

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능하다.
# 2. 똥은 화면 가장 위에 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character2.png
# 3. 똥 : 70 * 70 - ddong.png
import random
import pygame
###########################################################################
#! 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game") 

# FPS
clock = pygame.time.Clock()
###########################################################################

#* 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기 
background = pygame.image.load("arcadeGame/background.png")

# 캐릭터 만들기
character = pygame.image.load("arcadeGame/character2.png")
character = pygame.transform.scale(character, (70, 70))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 똥 만들기 
ddong = pygame.image.load("arcadeGame/ddong.png")
ddong = pygame.transform.scale(ddong, (70, 70))
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width) # 똥 가로값 뺀 값 
ddong_y_pos = 0
ddong_speed = 10 

running = True 
while running:
  dt = clock.tick(60)

  #* 2. 이벤트 처리 (키보드, 마우스 등)  
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.QUIT:
        running == False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed 
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0

  #* 3. 게임 캐릭터 위치 정의  
  character_x_pos += to_x

  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width
    
  ddong_y_pos += ddong_speed

  if ddong_y_pos > screen_height:
    ddong_y_pos = 0 
    ddong_x_pos = random.randint(0, screen_width - ddong_width)
    
  #* 4. 충돌 처리
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  ddong_rect = ddong.get_rect()
  ddong_rect.left = ddong_x_pos
  ddong_rect.top = ddong_y_pos
  
  if character_rect.colliderect(ddong_rect):
    print("충돌했어요")
    running = False
    
  #* 5. 화면에 그리기
  screen.blit(background, (0, 0))
  
  screen.blit(character, (character_x_pos, character_y_pos))
  
  screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

  pygame.display.update() # 게임화면 다시 그리기!

pygame.quit()