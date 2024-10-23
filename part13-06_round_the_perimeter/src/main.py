import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0

velocity = 1

clock = pygame.time.Clock()
# Movement direction: 0 = right, 1 = down, 2 = left, 3 = up

direction = 0


# Main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Fill the window with a black color
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    # Update the position of the robot based on the current direction
    if direction == 0:  # Moving right
        x += velocity
        if x + robot.get_width() >= 640:  # Right edge
            x = 640 - robot.get_width()  # Snap to the right edge
            direction = 1  # Change direction to down

    elif direction == 1:  # Moving down
        y += velocity
        if y + robot.get_height() >= 480:  # Bottom edge
            y = 480 - robot.get_height()  # Snap to the bottom edge
            direction = 2  # Change direction to left

    elif direction == 2:  # Moving left
        x -= velocity
        if x <= 0:  # Left edge
            x = 0  # Snap to the left edge
            direction = 3  # Change direction to up

    elif direction == 3:  # Moving up
        y -= velocity
        if y <= 0:  # Top edge
            y = 0  # Snap to the top edge
            direction = 0  # Change direction to right

    # Control the frame rate
    clock.tick(100) 