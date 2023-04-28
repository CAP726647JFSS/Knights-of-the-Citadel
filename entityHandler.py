import pygame


entities = pygame.sprite.Group()


class Entity(pygame.sprite.Sprite):
  
  def __init__(self, entity_image, max_health, castle=False):
    super().__init__()
    self.image = entity_image
    self.rect = self.image.get_rect()
    self.castle = castle
    entities.add(self)
    self.hitbox = self.rect
    self.max_health = max_health
    self.current_health = max_health
    #print("EntityCreated")

  def update_hitbox(self):
    self.hitbox = self.rect

  def get_hitbox(self):
    return self.hitbox

  def take_damage(self, damage):
    self.current_health -= damage
    if self.current_health <= 0:
        self.kill()

  def heal(self, amount):
    self.current_health += amount
    if self.current_health > self.max_health:
        self.current_health = self.max_health

  def is_alive(self):
    return self.current_health > 0

  def kill(self):
    super().kill()