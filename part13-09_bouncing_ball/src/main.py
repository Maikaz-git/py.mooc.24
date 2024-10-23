# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 320
y = 240
velocity_x = 2
velocity_y = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    window.blit(ball, (x, y))

    pygame.display.flip()

    x += velocity_x
    y += velocity_y

    if x + ball.get_width() >= 640 and velocity_x > 0:
        velocity_x = -velocity_x
    elif x <= 0 and velocity_x < 0:
        velocity_x = -velocity_x

    if y + ball.get_height() >= 480 and velocity_y > 0:
        velocity_y = -velocity_y
    elif y <= 0 and velocity_y < 0:
        velocity_y = -velocity_y

    clock.tick(60)