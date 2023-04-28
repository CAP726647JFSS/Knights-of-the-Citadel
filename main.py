import pygame, sys, random, math
from pygame.locals import *

from projectile import Projectile
from entityHandler import entities, Entity

# Initialize pygame and set display settings
pygame.init()
window = pygame.display.set_mode((900, 500))
asset_background_image = pygame.image.load('Assets/Tower/towerdefensebackground.jpg')
background_image = pygame.transform.scale(asset_background_image, (900, 500))
pygame.display.set_caption('Knights of the Citadel')

projectiles = []

castle_image = pygame.transform.scale(pygame.image.load('Assets/Tower/tower.png'), (85, 130))
basic_bullet_image = pygame.transform.scale(pygame.image.load('Assets/Bullets/light_bullet.png'), (10, 10))

castle = Entity(castle_image, 100, True)

def handle_collision(entity1, entity2):
 # Placeholder method - implement collision behavior here
 print(entity1, entity2)

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
      match projectileType:
        case "lightBullet":
          pos = [430 + math.cos(mouseAngle) * 25, 190 + math.sin(mouseAngle) * 25]
          vel = [math.cos(mouseAngle) * 10, math.sin(mouseAngle) * 10]
          size = 10
          damage = 10
          projectile = Projectile(pos, vel, size, damage, basic_bullet_image)
          projectiles.append(projectile)
        case "fireBall":
          pass
        case "lightningBolt"
          pass
        case "poisonCloud":
          pass
        case "holyHandGrenade":
          pass


  # update the projectiles
  for projectile in projectiles:
    projectile.update()
    if projectile.pos[0] < 0 or projectile.pos[0] > 900 or projectile.pos[1] < 0 or projectile.pos[1] > 500:
      projectile.kill()

  # draw the projectiles
  for projectile in projectiles:
    projectile.draw(window)

  collisions = pygame.sprite.groupcollide(entities, entities, False, False)
  for entity1, collided_entities in collisions.items():
    for entity2 in collided_entities:
      if entity1 != entity2:
        pass
        #print(entity1.rect, entity2.rect)


  pygame.event.pump()
  pygame.time.delay(50)
  pygame.display.update()
  




