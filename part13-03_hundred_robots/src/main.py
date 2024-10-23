# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()


window.fill((0,0,0))

for i in range(100):
    
    for rob in range(10):
        window.blit(robot, (random.randint(0,640-width) ,random.randint(0,480-height)))
   
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()