# Project 오락실 게임

```
python -m pip install beautifulsoup4
python -m pip install pygame
```

[게임 조건]
1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
2. 스페이스를 누르면 무기를 쏘아 올림
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
5. 모든 공을 없애면 게임 종료 (성공)
6. 캐릭터는 공에 닿으면 게임 종료 (실패)
7. 시간 제한 99초 초과 시 게임 종료 (실패)
8. FPS 는 30 으로 고정 (필요시 speed 값을 조정)

[게임 이미지]
1. 배경 : 640 * 480 (가로 세로) - background.png
2. 무대 : 640 * 50 - stage.png 
3. 캐릭터 : 60 * 60 - character.png
4. 무기 : 20 * 430 - weapon.png
5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 -  balloon1.png ~ balloon4.png 
