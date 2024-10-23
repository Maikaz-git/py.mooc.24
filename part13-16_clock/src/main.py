# WRITE YOUR SOLUTION HERE:
import pygame
import math
import datetime

pygame.init()

display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()








def convert_degrees_to_pygame(R, theta):
    y = math.cos(2*math.pi*theta/360) * R
    x = math.sin(2*math.pi*theta/360) * R
    return x+320, -(y-240)


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0,0,0))
    #Clock ring
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 220, 5)
    # Center ring
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 10)

    current_time  = datetime.datetime.now()
    seconds = current_time.second
    minute = current_time.minute
    hour = current_time.hour

    #minute
    R = 200
    theta = (minute+seconds/60) * (360/60)
    pygame.draw.line(display, (0, 0, 255), (320, 240), asdfasfd, 3)

    #second
    R = 210
    theta = seconds * (360/60)
    pygame.draw.line(display, (0, 0, 255), (320, 240), convert_degrees_to_pygame(R, theta), 1)
    #hour
    R = 150
    theta = (hour+minute/60+seconds/3600 )*(360/12)
    pygame.draw.line(display, (0, 0, 255), (320, 240), convert_degrees_to_pygame(R, theta), 7)


    pygame.display.update()
    clock.tick(50)