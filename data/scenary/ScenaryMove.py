import pygame

class ScenaryMove:
    def __init__(self, patchImg, width, height, speed):
        self.image = pygame.image.load(patchImg)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.posX1 = 0
        self.posX2 = width

        self.speed = speed

        self.marioDeath = False

    def update(self):
        if self.marioDeath:
            return
        self.posX1 -= self.speed
        self.posX2 -= self.speed

        if self.posX1 <= -self.image.get_width():
            self.posX1 = self.image.get_width()
        if self.posX2 <= -self.image.get_width():
            self.posX2 = self.image.get_width()

    def draw(self, screen):
        screen.blit(self.image, (self.posX1, 0))
        screen.blit(self.image, (self.posX2, 0))


