import pygame, sys, random, math
from pygame.locals import *

from projectile import Projectile

# Initialize pygame and set display settings
pygame.init()
window = pygame.display.set_mode((900, 500))
asset_background_image = pygame.image.load('Assets/Tower/towerdefensebackground.jpg')
background_image = pygame.transform.scale(asset_background_image, (900, 500))
pygame.display.set_caption('Knights of the Citadel')

circleX = 600
circleY = 600
projectiles = []

castle_image = pygame.transform.scale(pygame.image.load('Assets/Tower/tower.png'), (85, 130))
basic_bullet_image = pygame.transform.scale(pygame.image.load('Assets/Bullets/light_bullet.png'), (10, 10))


runGame = True
while runGame:

  window.fill((0, 0, 0))
  window.blit(background_image, (0,0))
  window.blit(castle_image, (385,168))
  
  mouseX, mouseY = pygame.mouse.get_pos()
  try:
    mouseAngle = math.atan2((mouseY - 190), (mouseX - 430))
  except ZeroDivisionError:
    mouseAngle = math.atan2((mouseY - 190), (mouseX - 429))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    # fire the projectile when the spacebar is pressed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        pos = [430 + math.cos(mouseAngle) * 25, 190 + math.sin(mouseAngle) * 25]
        vel = [math.cos(mouseAngle) * 20, math.sin(mouseAngle) * 20]
        size = 10
        projectile = Projectile(pos, vel, size, basic_bullet_image)
        projectiles.append(projectile)

  # update the projectiles
  for projectile in projectiles:
    projectile.update()
    if projectile.pos[0] < 0 or projectile.pos[0] > 900 or projectile.pos[1] < 0 or projectile.pos[1] > 500:
      projectiles.remove(projectile)

  # draw the projectiles
  for projectile in projectiles:
      projectile.draw(window)



  
  pygame.event.pump()
  pygame.time.delay(50)
  pygame.display.update()
  




