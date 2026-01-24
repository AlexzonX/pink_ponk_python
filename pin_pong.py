import pygame as pg
import sys
import random
#---------
pg.init()
pg.font.init()
#CONST
#-------
WIDTH = 800
HEIGHT = 990
#-------
text = "GAME OVER"
score = 0
ARIAL_FONT_PATH = pg.font.match_font('arial')
ARIAL_FONT_48 = pg.font.Font(ARIAL_FONT_PATH,48)
ARIAL_FONT_36 = pg.font.Font(ARIAL_FONT_PATH,36)
#-------
PLATFORM_WIDTH = 25
PLATFORM_HEIGHT = 100
PLATFORM_Speed = 8
#-------
pozition_rect = pg.rect.Rect(WIDTH /2 - PLATFORM_WIDTH /2,
                             HEIGHT - PLATFORM_HEIGHT *1,
                             PLATFORM_HEIGHT,
                             PLATFORM_WIDTH) 
#----------
CIRCLE_Speed = 5
CIRCLE_Speed_x = 0
CIRCLE_Speed_y = CIRCLE_Speed
CIRCLE_RADIUS = 15
circle_rect = pg.rect.Rect(WIDTH /2 - PLATFORM_WIDTH /2,
                             HEIGHT - PLATFORM_HEIGHT *3,
                             PLATFORM_HEIGHT,
                             PLATFORM_WIDTH)
Circle_first_random = False
#----------
TITLE = 'pin-pong'
FPS = 120
#Цвета 
WHITE = (255,255,255)
BLACK = (0, 0, 0)
#отрисовка экрана
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(TITLE)

#clock
clock = pg.time.Clock()
#GAME
running = True
game_over = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            game_over = True
            continue
        elif event.type == pg.K_ESCAPE:
            running = False
            game_over = True
            continue
    #--------------------
    if not game_over:
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            pozition_rect.x -= PLATFORM_Speed
        elif keys[pg.K_d]:
            pozition_rect.x += PLATFORM_Speed
        #-----------circle-runing---------
        if circle_rect.bottom >= HEIGHT:
            game_over = True
        elif circle_rect.top <= 0:
            CIRCLE_Speed_y += CIRCLE_Speed
            score += 1
        elif circle_rect.left  <= 0:
            CIRCLE_Speed_x += CIRCLE_Speed
        elif circle_rect.right  >= WIDTH:
            CIRCLE_Speed_x -= CIRCLE_Speed
        #-----edges------
        elif pozition_rect.left < 0:
            pozition_rect.left = 0
        elif pozition_rect.right > WIDTH:
            pozition_rect.right = WIDTH
        #----ciccle--for--rect--+--random-----
        if pozition_rect.colliderect(circle_rect):
            if not Circle_first_random:
                if random.randint(0, 1) == 0:
                    CIRCLE_Speed_x += CIRCLE_Speed
                else:
                    CIRCLE_Speed_x -= CIRCLE_Speed
                Circle_first_random = True
            CIRCLE_Speed_y -= CIRCLE_Speed
    #clear screen
    screen.fill(BLACK)
    #circle runing
    circle_rect.x += CIRCLE_Speed_x
    circle_rect.y += CIRCLE_Speed_y
    # draw something
    pg.draw.rect(screen,WHITE,(pozition_rect))
    pg.draw.circle(screen,WHITE,circle_rect.center,CIRCLE_RADIUS)
    #--screen--font--
    score_surface = ARIAL_FONT_48.render(str(score),True, WHITE)
    screen.blit(score_surface,[WIDTH /2 - score_surface.get_width() /2,15])
    #--screen--font--gameOver--
    if game_over == True:
        score_surface = ARIAL_FONT_48.render(str(text),True, WHITE)
        screen.blit(score_surface,[WIDTH /2 - score_surface.get_width() /2,450])
    #update screen
    pg.display.flip()
    #контролировать фпс
    clock.tick(FPS)


pg.quit()
sys.exit()    