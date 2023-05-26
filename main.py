import pygame, sys, random, math
from pygame.locals import *
import os
from projectile import Projectile
from entityHandler import entities, Entity
from enemy import Enemy


# Initialize pygame and set display settings
pygame.init()
window = pygame.display.set_mode((900, 500))
winWidth = 900
asset_background_image = pygame.image.load('Assets/Tower/towerdefensebackground.jpg')
background_image = pygame.transform.scale(asset_background_image, (900, 500))
pygame.display.set_caption('Knights of the Citadel')
clock = pygame.time.Clock()
testing_y_placement = random.randint(220, 300)
testing_x_placement = random.randint(20, 50)
#Instance of Enemy Class
enemies = []

timer = pygame.time.Clock()

left_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L8E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L9P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L10P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L11P.png"))
        ]
right_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R8E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R9P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R10P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R11P.png"))
        ]



projectiles = []
projectileList = ["lightBullet","fireBall","lightningBolt","poisonCloud","holyStrike"]
projectileType = 0

castle_image = pygame.transform.scale(pygame.image.load('Assets/Tower/tower.png'), (85, 130))
light_bullet_image = pygame.transform.scale(pygame.image.load('Assets/Bullets/light_bullet.png'), (10, 10))
fireball_bullet = [pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_1.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_2.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_3.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_4.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_5.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_6.png'), (40, 40))]
poison_cloud_bullet = pygame.transform.scale(pygame.image.load('Assets/Bullets/poison_cloud.png'), (150, 60))
lightning_bolt_bullet = pygame.transform.scale(pygame.image.load('Assets/Bullets/lightning_bolt.png'), (600, 10))
holy_strike_bullet = pygame.transform.scale(pygame.image.load('Assets/Bullets/holy_strike_overlay.png'), (1200, 800))

light_bullet_sound = pygame.mixer.Sound('Assets/SFX/light_bullet_cast.wav')

castle = Entity(castle_image, 100, True)
fps = 60
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
      for projectile in projectiles:
        if projectile.size == 3:
          projectiles.remove(projectile)
          projectile.kill()
      match projectileList[projectileType]:
        case "lightBullet":  # Medium damage medium speed
          pos = [430 + math.cos(mouseAngle) * 25, 190 + math.sin(mouseAngle) * 25]
          vel = [math.cos(mouseAngle) * 10, math.sin(mouseAngle) * 10]
          newProjectile = Projectile(pos, vel, 10, 10, light_bullet_image)
          projectiles.append(newProjectile)
          pygame.mixer.Sound.play(light_bullet_sound)
        case "fireBall":  # High damage lower speeds
          pos = [430 + math.cos(mouseAngle) * 25, 190 + math.sin(mouseAngle) * 25]
          vel = [math.cos(mouseAngle) * 5, math.sin(mouseAngle) * 5]
          newProjectile = Projectile(pos, vel, 11, 35, pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_1.png'), (15, 15)), fireball_bullet)
          projectiles.append(newProjectile)
        case "lightningBolt":  # high damage instant speed one
          pos = [430 + math.cos(mouseAngle) * 300, 190 + math.sin(mouseAngle) * 300]
          vel = [math.cos(mouseAngle) * 0.001, math.sin(mouseAngle) * 0.001]
          newProjectile = Projectile(pos, vel, 3, 100, lightning_bolt_bullet)
          projectiles.append(newProjectile)
        case "poisonCloud":  # Super slow large area low damage tick does not delete from collision
          pos = [430 + math.cos(mouseAngle) * 25, 190 + math.sin(mouseAngle) * 25]
          vel = [math.cos(mouseAngle) * 1, math.sin(mouseAngle) * 1]
          newProjectile = Projectile(pos, vel, 15, 1, poison_cloud_bullet)
          projectiles.append(newProjectile)
        case "holyStrike":  # Summons mapwide projectile super high damage
          pos = [430 + math.cos(mouseAngle), 190 + math.sin(mouseAngle)]
          vel = [math.cos(mouseAngle) * 0, math.sin(mouseAngle) * 0]
          newProjectile = Projectile(pos, vel, 99, 999, holy_strike_bullet)
          projectiles.append(newProjectile)


  # update the projectiles
  for projectile in projectiles:
    projectile.update()
    hit_enemies = []  # List to store the enemies hit by the projectile
    for enemy in enemies:
        if projectile.rect.colliderect(enemy.rect):
            enemy.health -= projectile.damage
            hit_enemies.append(enemy)
            if projectile.size != 15 and projectile.size != 3 and projectile.size != 99:
                try:
                    projectiles.remove(projectile)
                    projectile.kill()
                except ValueError:
                  pass
    # Remove the hit enemies from the main enemy list
    
  # draw the projectiles
  for projectile in projectiles:
    projectile.draw(window)

#Check on how 
# (879, 147)
  if len(enemies) == 0:
    rand_nr = random.randint(0, 1)
    if rand_nr == 1:
      for j in range(1):
        enemy_left_two = Enemy(870, 150, 'left')
        enemy_left_three = Enemy(890, 180, 'left')
        enemy_left_four = Enemy(875, 145, 'left')     
      enemy = Enemy(850, 200, 'left')
      enemies.append(enemy)
      enemies.append(enemy_left_two)
      enemies.append(enemy_left_three)
      enemies.append(enemy_left_four)
    if rand_nr == 0:
      for i in range(1):
        enemytwo = Enemy(5, 100, 'right')
        enemythree = Enemy(5, 50, 'right')
      enemies.append(enemytwo)
      enemies.append(enemythree)
      enemy = Enemy(10, 70, 'right')
      enemies.append(enemy)
  for enemy in enemies:
    enemy.move()
    enemy.stepIndex += 1
    if enemy.stepIndex >= 40:
      enemy.stepIndex = 0
    if enemy.off_screen() or enemy.health <= 0:
      enemies.remove(enemy)


      
  for enemy in enemies: 
    enemy.draw(window)
  pygame.event.pump()
  pygame.time.delay(10)
  pygame.display.update()
  for projectile in projectiles:
    if projectile.size == 3 or projectile.size == 99:
        pygame.time.delay(20)
        projectiles.remove(projectile)
        projectile.kill()
  




