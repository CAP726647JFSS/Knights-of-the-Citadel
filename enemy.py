import pygame
import os
import random

win_width = 900
win_height = 500
#Instance of Enemy Class
enemies = []



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

class Enemy: 
  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.direction = direction
    self.stepIndex = 0
    self.health = 100
    self.width = 55  # Adjust the width of the enemy
    self.height = 55  # Adjust the height of the enemy
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Create the rect object
    self.path = []  # List to store the path coordinates
    self.calculatePath()  # Calculate the path for the enemy
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
  def step(self):
    if self.stepIndex >= 55:
      self.stepIndex = 0

  def calculatePath(self):
 # Calculate the path for the enemy to follow

    # Calculate a simple linear path from the enemy's current position to the target position
    if self.direction == 'left':
      path_points = [
      (self.x, self.y),       
      (879, 147), 
      (854, 130), 
      (814, 112), 
      (779, 109), 
      (670, 109), 
      (612, 119),
      (585, 132),
        (580, 160), (560, 202), (540, 260),(450, 250)
  ]

      self.path = path_points
    elif self.direction == 'right':
        self.path = [(self.x, self.y), (9, 73), (30, 79), (35, 138), (69, 179), (90, 194), (127, 195), (234, 195), (269, 199), (300, 222), (320, 237), (380, 230)]


  def move(self):
    # Move the enemy along the calculated path
    if self.path:
      target_x, target_y = self.path[0]
      if self.x < target_x:
          self.x += 0.5
      elif self.x > target_x:
          self.x -= 0.5
      if self.y < target_y:
          self.y += 0.5
      elif self.y > target_y:
          self.y -= 0.5
      self.rect.x = self.x
      self.rect.y = self.y
      if self.x == target_x and self.y == target_y:
          self.path.pop(0)  # Remove the current target from the path
  def draw(self, win):
      self.step()
      self.move()
    #Left is when enemies are moving towards the left side
      if self.direction == 'left':
        win.blit(left_enemy[self.stepIndex // 10], (self.x, self.y))
    #Right is when enemies are moving towards the right side
      if self.direction == 'right':
        win.blit(right_enemy[self.stepIndex // 10], (self.x, self.y))
        self.stepIndex = (self.stepIndex + 1) % (len(left_enemy) * 10)

  # Health bar variables
      health_bar_width = 50
      health_bar_height = 5
      health_bar_x = self.x + (self.width - health_bar_width) // 2
      health_bar_y = self.y - health_bar_height - 2
      health_bar_fill = (self.health / 100) * health_bar_width
  
      # Draw health bar
      health_bar_outline = pygame.Rect(health_bar_x, health_bar_y, health_bar_width, health_bar_height)
      health_bar_fill_rect = pygame.Rect(health_bar_x, health_bar_y, health_bar_fill, health_bar_height)
  
      pygame.draw.rect(win, (255, 0, 0), health_bar_outline)
      pygame.draw.rect(win, (0, 255, 0), health_bar_fill_rect)

  def off_screen(self):
    return not(self.x >= -55 and self.x <= win_width)

  def is_collision(self, projectile):
          # Calculate the distance between the center of the enemy and the center of the projectile
          distance = ((self.x + self.radius) - (projectile.pos[0] + projectile.width / 2)) ** 2 + \
                     ((self.y + self.radius) - (projectile.pos[1] + projectile.height / 2)) ** 2
          # Check if the distance is less than the sum of the radii of the enemy and the projectile
          return distance < (self.radius + max(projectile.width, projectile.height)) ** 2
  



