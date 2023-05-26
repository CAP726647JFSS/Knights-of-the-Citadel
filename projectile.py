import pygame
import math
from entityHandler import entities, Entity

class Projectile(pygame.sprite.Sprite):  
  def __init__(self, pos, vel, size, damage, sprite_image, sprite_frames = []):
    super().__init__()
    self.sprite = sprite_image
    self.pos = pos
    self.vel = vel
    self.size = size
    if self.size != 15:
      self.angle = math.degrees(math.atan2(self.vel[1], self.vel[0]))
    else:
      self.angle = 0
    self.image = pygame.transform.rotate(self.sprite, -self.angle)
    self.rect = self.image.get_rect(center=pos)
    self.damage = damage
    if sprite_frames == []:
      self.sprite_frames = [sprite_image]
    else:
      self.sprite_frames = sprite_frames
    self.frame = 0
    self.animation_speed = 5
    self.frame_counter = 0
    entities.add(self)

  def update(self):
    self.pos[0] += self.vel[0]
    self.pos[1] += self.vel[1]
    self.angle = math.degrees(math.atan2(self.vel[1], self.vel[0]))
    self.frame_counter += 1
    if self.frame_counter >= self.animation_speed:
        self.frame_counter = 0
        self.frame = (self.frame + 1) % len(self.sprite_frames)
        self.sprite = self.sprite_frames[self.frame]
        if self.size != 15:
          self.image = pygame.transform.rotate(self.sprite, -self.angle)
        self.rect = self.image.get_rect(center=self.pos)

  def draw(self, surface):
    surface.blit(self.image, self.rect)

  def kill(self):
    super().kill()