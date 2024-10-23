# WRITE YOUR SOLUTION HERE:
import pygame


pygame.init()
window = pygame.display.set_mode((640, 480))


robot = pygame.image.load("robot.png")
x1 = 0
y1 = 480-robot.get_height()

x2 = 50
y2 = 200

to_right = False
to_left = False
to_up = False
to_down = False

to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                to_up2 = True
            if event.key == pygame.K_s:
                to_down2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                to_up2 = False
            if event.key == pygame.K_s:
                to_down2 = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x1 < 590 :
        x1 += 2
    if to_left and x1 > 0:
        x1 -= 2
    if to_up  and y1 > 0:
        y1 -= 2
    if to_down and y1 < 390:
        y1 += 2


    if to_right2 and x2 < 590 :
        x2 += 2
    if to_left2 and x2 > 0:
        x2 -= 2
    if to_up2  and y2 > 0:
        y2 -= 2
    if to_down2 and y2 < 390:
        y2 += 2


    window.fill((0,0,0))
    window.blit(robot, (x1,y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)