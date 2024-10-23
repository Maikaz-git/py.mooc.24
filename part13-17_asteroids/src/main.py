import pygame
from random import randint
import sys

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Asteroids")f

rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")

# number of rocks (the same rocks are reused)
number = 6

rocks = []
for i in range(number):
    # causes the new random start position to be drawn immediately
    rocks.append([-700, height])

robot_x = (width - robot.get_width()) //2
robot_y = height - robot.get_height()
robot_speed = 5


# initialize the score
score = 0
# font obj
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # get the current key presses
    keys = pygame.key.get_pressed()

    # move robot left and right
    if keys[pygame.K_LEFT]:
        robot_x -= robot_speed
    if keys[pygame.K_RIGHT]:
        robot_x += robot_speed

    # so robot doesn't move off the screen
    robot_x = max(0, min(robot_x, width - robot.get_width()))

    # move rocks
    for i in range(number):
        if rocks[i][1]  < height:
            # the rock falls downwards
            rocks[i][1] += 1
        else:
            if rocks[i][0] < -rock.get_width() or rocks[i][0] > width:
                # new random start point
                rocks[i][0] = randint(0, width-rock.get_width())
                rocks[i][1] = -randint(100, 1000)
                


        # check for collision between rock and robot
        rock_rect = pygame.Rect(rocks[i][0], rocks[i][1], rock.get_width(), rock.get_height())
        robot_rect = pygame.Rect(robot_x, robot_y, robot.get_width(), robot.get_height())
        if rock_rect.colliderect(robot_rect):
            
            # you can increment the score here, or perform any other action
            score += 1 
            rocks[i] = [-1000, height]  # reset the rock's position
          # Check if the rock hits the bottom of the screen
        if rock_rect.bottom >= height:
            print("Game Over!")
            pygame.quit()
            sys.exit()


    screen.fill((0, 0 , 0))
    screen.blit(robot, (robot_x, robot_y))
    for i in range(number):
        screen.blit(rock, (rocks[i][0], rocks[i][1]))


    # render the score text
    score_text = font.render(f"Score: {score}", True, (255,0,0))
    screen.blit(score_text, (width-150, 10))
    pygame.display.flip()

    clock.tick(60)