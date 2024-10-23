# Complete your game here
# "A rain of coins"

# FINAL VERSION

import pygame
from random import randint

class CoinRain:
    def __init__(self):
        pygame.init()
        self.width, self.height = 640, 480
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Coin Rain")

        self.robot = pygame.image.load("robot.png")
        self.x = 0
        self.y = self.height - self.robot.get_height()

        self.coin = pygame.image.load("coin.png")
        self.monster = pygame.image.load("monster.png")
        self.number = 4
        self.coin_positions = self.initialize_positions(self.coin)
        self.monster_positions = self.initialize_positions(self.monster, self.number // 3) 
 
        self.to_right = False
        self.to_left = False

        self.points = 0

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)

    def initialize_positions(self, image , num=None):
        if num is None:
            num = self.number
        positions = []
        for i in range(num):
            positions.append([randint(0, self.width - image.get_width()), -randint(100, 1000)])
        return positions

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
            if event.type == pygame.QUIT:
                exit()

   
    def update(self):
        if self.to_right:
            self.x += 2
        if self.to_left:
            self.x -= 2

        for i in range(self.number):
            self.coin_positions[i][1] += 1
            if self.coin_positions[i][1] + self.coin.get_height() >= self.height:
                # game ends
                exit()
            if self.coin_positions[i][1] + self.coin.get_height() >= self.y:
                robot_middle = self.x + self.robot.get_width() / 2
                rock_middle = self.coin_positions[i][0] + self.coin.get_width() / 2
                if abs(robot_middle - rock_middle) <= (self.robot.get_width() + self.coin.get_width()) / 2:
                    # the robot caught an asteroid
                    self.coin_positions[i][0] = randint(0, self.width - self.coin.get_width())
                    self.coin_positions[i][1] = -randint(100, 1000)
                    self.points += 1

        for i in range(len(self.monster_positions)):
            self.monster_positions[i][1] += 1
                
            if self.monster_positions[i][1] + self.monster.get_height() >= self.y:
                robot_middle = self.x + self.robot.get_width() / 2
                monster_middle = self.monster_positions[i][0] + self.monster.get_width() / 2
                if abs(robot_middle - monster_middle) <= (self.robot.get_width() + self.monster.get_width()) / 2:
                    # the robot hit a monster
                    exit()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.robot, (self.x, self.y))
        for i in range(self.number):
            self.screen.blit(self.coin, (self.coin_positions[i][0], self.coin_positions[i][1]))

        for i in range(len(self.monster_positions)):
            self.screen.blit(self.monster, (self.monster_positions[i][0], self.monster_positions[i][1]))

        text = self.font.render("Points: " + str(self.points), True, (255, 0, 0))
        self.screen.blit(text, (self.width - 150, 10))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clffqfock.tick(60)

if __name__ == "__main__":
    game = CoinRain()
    game.run()

