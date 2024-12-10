import pygame # type: ignore

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = [
            pygame.transform.scale(pygame.image.load("data/assets/mariowalking2.png").convert_alpha(), (40, 40)),
            pygame.transform.scale(pygame.image.load("data/assets/mariowalking.png").convert_alpha(), (40, 40)),
            pygame.transform.scale(pygame.image.load("data/assets/mariojumping.png").convert_alpha(), (40, 40)),
            pygame.transform.scale(pygame.image.load("data/assets/mariodeath.png").convert_alpha(), (40, 40))

        ]
        self.currentSprite = 0  
        self.image = self.sprites[self.currentSprite]  
        self.rect = self.image.get_rect()  
        self.rect.topleft = (40, 523)  
        self.playerSpeed = 5 
        self.deathState = False
        self.noDobleJump = False
        #self.doubleJump = False

        ## JUMP
        self.flying = False
        self.speedJump = -10
        self.gravity = 0.8
        self.speedY = 0
        self.floor = 523  

        self.animationTime = 100  
        self.lastUpdate = pygame.time.get_ticks() 


        self.lastTick = pygame.time.get_ticks()

    def moving(self, keys):
        if self.deathState:
            return
        isMoving = True

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.playerSpeed
            if self.rect.x <= 10:
                self.rect.x = 10
            self.animationTime = 200
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.playerSpeed
            if self.rect.x >= 740:
                self.rect.x = 740
            self.animationTime = 50
        if keys[pygame.K_UP]:# and not self.flying:
            now = pygame.time.get_ticks()
            if self.flying == False:
                #print("Saving tick... ", self.lastTick)
                self.lastTick = now
            
            if now - self.lastTick > 200:
                #print ("--------------------------> No Double Jump")
                #print("---------------------------> Live tick... ", now)
                #print("---------------------------> Last tick... ", self.lastTick)
                self.noDobleJump = True

            if self.rect.y >= 400:
                self.jump()
                #print(now)
            else:
                self.noDobleJump = True


                


                

        if isMoving:
            self.updateSprites()

        self.applyGravity()
        self.animationTime = 100

    def applyGravity(self):
        if self.deathState:
            return

        self.speedY += self.gravity # 1o frame: -10 + 0.4 = -9.6 | 2o frame: -9.6 + 0.4 = -9.2 | 3o frame: -9.2 + 0.4 = -8.8 | 4o frame: -8.8 + 0.4 = -8.4 | 5o frame: -8.4 + 0.4 = -8.0
        self.rect.y += self.speedY # 1o frame: 485 + (-9.6) = 475.4 | 2o frame: 475.4 + (-9.2) = 466.2 | 3o frame: 466.2 + (-8.8) = 457.4 | 4o frame: 457.4 + (-8.4) = 449.0 | 5o frame: 449.0 + -(8.0) = 441.0

        if self.rect.y >= self.floor:
            self.rect.y = self.floor
            self.speedY = 0
            self.flying = False
            self.noDobleJump = False

    def jump(self):    
        if self.noDobleJump:
            self.speedY += 0
            self.flying = True
        else:
            self.speedY = self.speedJump
            self.flying = True


    def updateSprites(self):
        if self.flying:
            self.image = self.sprites[2]
            return
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.animationTime:
            self.lastUpdate = now
            self.currentSprite = 0 if self.currentSprite == 1 else 1
            self.image = self.sprites[self.currentSprite]



    def death(self, scenary):
        self.currentSprite = 3
        self.image = self.sprites[self.currentSprite]
        self.deathState = True
        scenary.marioDeath = True
            