import pygame # type: ignore

class FireBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = [
            pygame.transform.scale(pygame.image.load("data/assets/enemy1.png").convert_alpha(), (70, 70)),
            pygame.transform.scale(pygame.image.load("data/assets/enemy2.png").convert_alpha(), (70, 70))

        ]
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (800, 490)
        self.enemySpeed = -5
        self.marioDeath = False

        self.animationsTime = 250
        self.lastUpdate = pygame.time.get_ticks()


    def moving (self, width, scenario):
        if scenario.marioDeath:
            return

        if self.rect.x >= -55:
            self.rect.x += self.enemySpeed
        if self.rect.x <= -55:
            self.rect.x =  width
        self.updateSprites()

    def updateSprites(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.animationsTime:
            self.lastUpdate = now
            self.currentSprite = 0 if self.currentSprite == 1 else 1
            self.image = self.sprites[self.currentSprite]

    def playerCollision(self, player, scenary):
        if self.rect.x - 30 <= player.rect.x and self.rect.x + 30 >= player.rect.x and self.rect.y - 40 < player.rect.y:
            player.death(scenary)