import pygame

class Widget:
  def __init__(self, _sprite, _parentUI, _posX = 0, _posY = 0):
    self.parent = _parentUI
    self.sprite = pygame.image.load(_sprite)
    self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width(), self.sprite.get_height()))
    self.widgetRect = self.sprite.get_rect()
    self.widgetRect.topleft = (_posX, _posY)
  def update(self):
    self.parent.blit(self.sprite, self.widgetRect)