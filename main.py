import pygame
import os
import random

pygame.init()
screen=pygame.display.set_mode((640,640))
pygame.display.set_caption("SNAKE GAME")
clock=pygame.time.Clock()
file_path=os.path.dirname(__file__)
image_path=os.path.join(file_path,("image"))
game_font=pygame.font.Font(None,40)

# 배경화면 로드
background=pygame.image.load(os.path.join(image_path,"background.png"))# 검은 배경
board_size=20 # 스테이지 크기

# 스네이크 초기화
piece_size=32 # 몸통 조각 크기
snake_piece=pygame.image.load(os.path.join(image_path,"snake.png")) # 몸통 이미지

# 스네이크 좌표
snake_body=[[int(board_size/2)-5,int(board_size/2)]]
snake_body.append([snake_body[0][0]-1,snake_body[0][1]])
snake_body.append([snake_body[1][0]-1,snake_body[1][1]])

move=[[1,0],[-1,0],[0,1],[0,-1]]
snake_move=0

# 먹이 초기화
feed=pygame.image.load(os.path.join(image_path,"feed.png"))
feed_pos=[0,0]
while True:
    feed_pos[0]=random.randrange(0,20)
    feed_pos[1]=random.randrange(0,20)
    for s in snake_body:
        if feed_pos[0]==s[0] and feed_pos[1]==s[1]:
            break
    else:
        break

score=0

# 메인 루프
run=True
while run:
    fps=clock.tick(8)
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if snake_move!=1:
                    snake_move=0
            if event.key==pygame.K_LEFT:
                if snake_move!=0:
                    snake_move=1
            if event.key==pygame.K_DOWN:
                if snake_move!=3:
                    snake_move=2
            if event.key==pygame.K_UP:
                if snake_move!=2:
                    snake_move=3
    
    # 스네이크 이동
    head_pos_x=snake_body[0][0]+move[snake_move][0]
    head_pos_y=snake_body[0][1]+move[snake_move][1]

    # 벽에 충돌
    if head_pos_x<0 or head_pos_x>=board_size:
        run=False
        break
    if head_pos_y<0 or head_pos_y>=board_size:
        run=False
        break

    # 자신과 충돌
    for s in snake_body:
        if s[0]==head_pos_x and s[1]==head_pos_y:
            run=False
            break
    if not run:
        break

    # 이동한 좌표 저장
    snake_body.insert(0,[head_pos_x,head_pos_y])

    # 먹이를 먹음
    if feed_pos[0]==head_pos_x and feed_pos[1]==head_pos_y:
        score+=1
        while True:
            feed_pos[0]=random.randrange(0,20)
            feed_pos[1]=random.randrange(0,20)
            for s in snake_body:
                if feed_pos[0]==s[0] and feed_pos[1]==s[1]:
                    break
            else:
                break
    else:
        snake_body.pop()

    # 화면 출력
    screen.blit(background,(0,0))
    screen.blit(feed,(feed_pos[0]*piece_size,feed_pos[1]*piece_size))
    for s in snake_body:
        s_pos_x=s[0]*piece_size
        s_pos_y=s[1]*piece_size
        screen.blit(snake_piece,(s_pos_x,s_pos_y))

    screen.blit(game_font.render("Score : {}".format(int(score)),True,(0,0,0)),(10,10))

    pygame.display.update()

game_over=game_font.render("GAME OVER".format(int(score)),True,(255,0,0))
game_over_size=game_over.get_rect().size
screen.blit(game_over,(320-(game_over_size[0]/2),320-(game_over_size[1])/2))
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()