import pygame

class Button:
  def __init__(self, _onClick, _sprite, _parentUI, _posX = 0, _posY = 0):
    self.parent = _parentUI
    self.sprite = pygame.image.load(_sprite)
    self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width(), self.sprite.get_height()))
    self.buttonRect = self.sprite.get_rect()
    self.buttonRect.topleft = (_posX, _posY)
    self.buttonSurface = pygame.Surface((self.sprite.get_width(), self.sprite.get_height()))
    self.onClick = _onClick
    self.pressed = False

  def update(self):
    mousePos = pygame.mouse.get_pos()
    self.buttonSurface.set_alpha(255)
    self.buttonSurface.blit(self.sprite, (0,0))
    if self.buttonRect.collidepoint(mousePos):
      self.buttonSurface.set_alpha(200)
      if pygame.mouse.get_pressed(num_buttons=3)[0]:
        self.buttonSurface.set_alpha(160)
        if not self.pressed:
          self.onClick()
          self.pressed = True
      else:
        self.pressed = False
    self.parent.blit(self.buttonSurface, (self.buttonRect.x, self.buttonRect.y))