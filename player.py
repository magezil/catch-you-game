import pygame

from constants import HEIGHT, WIDTH

class Player:
    def __init__(self, image, height, speed):
        self.image = image
        self.speed = speed
        self.height = height
        self.pos = image.get_rect().move(0, height)
    
    def move(self, keys):
        # self.pos = self.pos.move(self.speed, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.pos.top -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.pos.top += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.pos.right -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.pos.right += self.speed
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT-self.height:
            self.pos.top = 0
        if self.pos.right < self.height:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT-self.height
    