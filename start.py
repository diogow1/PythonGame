import os
import pygame # type: ignore
import sys
from data.scenary.ScenaryMove import ScenaryMove
from data.scenary.ScenaryClouds import ScenaryClouds
from data.player.Player import Player
from data.enemys.FireBall import FireBall


pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Mario")

gameFinish = False

scenary = ScenaryMove("data/assets/blocks.PNG", width, height, 3)
scenaryClouds = ScenaryClouds("data/assets/clouds.PNG", width, 350, 2)

player = Player()
fireball = FireBall()
fireBallTwo = FireBall()


sprites = pygame.sprite.Group()
sprites.add(player)
sprites.add(fireball)
sprites.add(fireBallTwo)
scenary.scenaryTheme()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    currentTime = pygame.time.get_ticks()
    scenary.draw(screen)
    scenaryClouds.draw(screen)

    scenary.update()
    scenaryClouds.update(scenary)

    if currentTime - player.deathTick > 500 and player.deathState == True and scenary.scenaryPause== True:
        print("oh!")
        scenary.scenaryPause = False
        player.deathAnimation()
        

    if scenary.scenaryPause== False:
        keys = pygame.key.get_pressed()
        player.moving(keys)
        fireball.moving(width, scenary)
        fireball.playerCollision(player, scenary)



    if currentTime > 2000:
        fireBallTwo.moving(width, scenary)
        fireBallTwo.playerCollision(player, scenary)


    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)






## Reference: https://www.pygame.org/docs/
##            https://www.mariouniverse.com/sprites-gba-smb3/