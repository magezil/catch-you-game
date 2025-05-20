# Example file showing a circle moving on screen
import os
import random

import pygame

from constants import WIDTH, HEIGHT, SPEED
from player import Player

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

def load_image(name, colorkey=None, scale=.1):
    fullname = os.path.join(data_dir, name)
    # return pygame.image.load(fullname).convert()
    image = pygame.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image #, image.get_rect()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

doughnut_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# doughnut_pos = pygame.Vector2(player_pos.x + 80, player_pos.y - 80)
player = load_image("PXL_20250505_182832275.jpg")
player_object = Player(player, 40, SPEED)
direction = random.randint(0, 3)
count = 0
change_dir = 10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    # draw doughnut
    pygame.draw.circle(screen, "pink", doughnut_pos, 40)
    pygame.draw.circle(screen, "purple", doughnut_pos, 20)

    keys = pygame.key.get_pressed()
    player_object.move(keys)
    screen.blit(player_object.image, player_object.pos)

    if count == change_dir:
        direction = random.randint(0, 3)
        count = 0
    else:
        count +=1
    # print(direction)
    
    if direction == 0:
        doughnut_pos.y -= SPEED
    elif direction == 1:
        doughnut_pos.y += SPEED
    elif direction == 2:
        doughnut_pos.x -= SPEED
    else:
        doughnut_pos.x += SPEED

    # pygame.display.update()
    # if keys[pygame.K_w] or keys[pygame.K_UP]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s] or keys[pygame.K_DOWN]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    #     player_pos.x += 300 * dt

    # # flip() the display to put your work on screen
    pygame.display.flip()

    # # limits FPS to 60
    # # dt is delta time in seconds since last frame, used for framerate-
    # # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
