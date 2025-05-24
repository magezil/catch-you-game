from constants import HEIGHT, WIDTH

class GameObject:
    def __init__(self, image, height, speed, pos):
        self.image = image
        self.speed = speed
        self.height = height
        self.pos = image.get_rect().move(pos)
    
    def move(self, direction):
        # self.pos = self.pos.move(self.speed, 0)

        if direction == 0:
            self.pos.top -= self.speed
        elif direction == 1:
            self.pos.top += self.speed
        elif direction == 2:
            self.pos.right -= self.speed
        else:
            self.pos.right += self.speed
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT-self.height:
            self.pos.top = 0
        if self.pos.right < self.height:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT-self.height

    def check_collision(self, other):
        return self.pos.colliderect(other.pos)
    