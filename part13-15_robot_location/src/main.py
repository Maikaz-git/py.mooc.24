# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))


robot = pygame.image.load("robot.png")

robot_x = random.randint(40, 600)
robot_y = random.randint(40, 440)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
         
            mouse_x, mouse_y = event.pos


            # Check if the user clicked on the robot
            if (mouse_x >= robot_x and mouse_x <= robot_x + robot.get_width() and
                 mouse_y >= robot_y and mouse_y <= robot_y + robot.get_height()):

                # Move the robot to a new random location
                robot_x = random.randint(40, 600)
                robot_y = random.randint(40, 440)


    # Draw everything
    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)