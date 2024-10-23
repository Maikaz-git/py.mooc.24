# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x1 = 0
y1 = 100
velocity_x1 = 1


x2 = 0
y2 = 200
velocity_x2 = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))

    pygame.display.flip()
    x1 += velocity_x1
    x2 += velocity_x2

    if x1 + robot.get_width() >= 640 and velocity_x1 > 0:
        velocity_x1 = -velocity_x1
    elif x1 <= 0 and velocity_x1 < 0:
        velocity_x1 = -velocity_x1

    if x2 + robot.get_width() >= 640 and velocity_x2 > 0:
        velocity_x2 = -velocity_x2
    elif x2 <= 0 and velocity_x2 < 0:
        velocity_x2 = -velocity_x2

    clock.tick(60)