# Example file showing a circle moving on screen
import random
import pygame

from constants import WIDTH, HEIGHT, SPRITE_WIDTH
from game_object import GameObject
from utils import load_image

BACKGROUND_COLOR = "purple"

# pygame setup
pygame.init()
pygame.display.set_caption("Catch you game!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BACKGROUND_COLOR)
caught_text = None

if pygame.font:
    font = pygame.font.Font(None, 64)
    text = font.render("Catch Falkor!", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = load_image("PXL_20250505_182832275.jpg")
player_speed = 10
player_object = GameObject(player, SPRITE_WIDTH, player_speed, player_pos)

catcher_pos = pygame.Vector2(player_pos.x - 80, player_pos.y + 80)
catcher = load_image("IMG_20210324_152518.jpg", -1, scale=0.1)
catcher_speed = 10
catcher_object = GameObject(catcher, SPRITE_WIDTH, catcher_speed, catcher_pos)

doughnut_pos = pygame.Vector2(player_pos.x + 80, player_pos.y)
doughnut = pygame.Surface((SPRITE_WIDTH, SPRITE_WIDTH))
doughnut.fill(BACKGROUND_COLOR) # background of doughnut should be same as the background color
pygame.draw.circle(doughnut, "pink", [SPRITE_WIDTH/2,SPRITE_WIDTH/2], SPRITE_WIDTH/2, SPRITE_WIDTH//4)
doughnut_speed = 13
doughnut_object = GameObject(doughnut, SPRITE_WIDTH, doughnut_speed, doughnut_pos)

direction = random.randint(0, 3)
count = 0
change_dir = 10
start = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            start = True
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        catcher_object.move(0)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        catcher_object.move(1)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        catcher_object.move(2)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        catcher_object.move(3)
    screen.blit(doughnut_object.image, doughnut_object.pos)
    screen.blit(player_object.image, player_object.pos)
    screen.blit(catcher_object.image, catcher_object.pos)

    if start:
        if count == change_dir:
            direction = random.randint(0, 3)
            count = 0
        else:
            count +=1

        if direction == 0:
            doughnut_object.move(0)
        elif direction == 1:
            doughnut_object.move(1)
        elif direction == 2:
            doughnut_object.move(2)
        else:
            doughnut_object.move(3)

        if count == 0:
            direction = random.randint(0, 3)
        if direction == 0:
            player_object.move(0)
        elif direction == 1:
            player_object.move(1)
        elif direction == 2:
            player_object.move(2)
        else:
            player_object.move(3)
        
        caught = catcher_object.check_collision(player_object)
        if caught and pygame.font:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            caught_text = font.render("Caught you!", True, (r, g, b))
            caught_textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() / 2)
            screen.blit(caught_text, caught_textpos)


    # # flip() the display to put your work on screen
    pygame.display.flip()

    # # limits FPS to 60
    # # dt is delta time in seconds since last frame, used for framerate-
    # # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
