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

runGame = True
while runGame:

  window.fill((0, 0, 0))
  window.blit(background_image, (0,0))
  
  mouseX, mouseY = pygame.mouse.get_pos()
  try:
    mouseAngle = math.atan2((mouseY - 250), (mouseX - 450))
  except ZeroDivisionError:
    mouseAngle = math.atan2((mouseY - 250), (mouseX - 449))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    # fire the projectile when the spacebar is pressed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        pos = [450, 250]
        vel = [math.cos(mouseAngle), math.sin(mouseAngle)]
        size = 10
        projectile = Projectile(pos, vel, size)
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
  




