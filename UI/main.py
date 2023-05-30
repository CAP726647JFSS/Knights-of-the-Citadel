# https://www.youtube.com/watch?v=f29ZOu4rXlM
#https://www.google.com/search?q=menu+buttons&tbm=isch&ved=2ahUKEwj0ybXw1ov_AhUXElkFHSTqBxsQ2-cCegQIABAA&oq=menu+buttons&gs_lcp=CgNpbWcQAzIHCAAQigUQQzIHCAAQigUQQzIHCAAQigUQQzIFCAAQgAQyBwgAEIoFEEMyBwgAEIoFEEMyBQgAEIAEMgcIABCKBRBDMgcIABCKBRBDMgUIABCABFDjFVjjFWCmF2gAcAB4AIABhwGIAYcBkgEDMC4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=ZNFsZPSHBZek5NoPpNSf2AE&bih=1032&biw=1903&rlz=1C1GCEA_enCA1059&safe=active&hl=en-US#imgrc=0-hfIaHGGSk1JM
#https://www.youtube.com/watch?v=wkrXbl1RlAg&ab_channel=FHCoding


import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Knights of the Citadel!')

class Widget:
  def __init__(self, _sprite, _posX = 0, _posY = 0):
    self.sprite = pygame.image.load(_sprite)
    self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width(), self.sprite.get_height()))
    self.widgetRect = self.sprite.get_rect()
    self.widgetRect.topleft = (_posX, _posY)

  def update(self):
    DISPLAYSURF.blit(self.sprite, self.widgetRect)

class Button:
  def __init__(self, _onClick, _sprite, _posX = 0, _posY = 0):
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
    DISPLAYSURF.blit(self.buttonSurface, (self.buttonRect.x, self.buttonRect.y))


background_color = (255,255,255)
def test_onclick():
  print("Ow")
#Button(test_onclick, "main_menu.png")

class Menu:
  objects = []
  def __init__(self, _visible):
    self.visible = _visible
    self.uiElements = []

class MainMenu(Menu):
  def __init__(self, _visible):
    super().__init__(_visible)
    #self.playmenu = Widget("playmenu.jpg")
    self.background = Widget("background.png", 0, 0)
    self.menuBackground = Widget("menubackground.png", 100, -50)
    self.play = Button(playButton, "playbutton2.png", 230, 160)
    self.settings = Button(playButton, "settingsbutton2.png", 230, 260)
    self.credits = Button(playButton, "creditsbutton2.png", 230, 360)
    self.quit = Button(quitButton, "quitbutton2.png", 230, 460)
    self.logo = Widget("logo.png", 1770, 0)
    #self.uiElements.append(self.playmenu)
    self.uiElements.append(self.background)
    self.uiElements.append(self.menuBackground)
    self.uiElements.append(self.play)
    self.uiElements.append(self.settings)
    self.uiElements.append(self.credits)
    self.uiElements.append(self.quit)
    self.uiElements.append(self.logo)
    Menu.objects.append(self)
  def update(self):
    DISPLAYSURF.fill((32,33,38))
    for uiElement in self.uiElements:
      uiElement.update()

class OtherMenu(Menu):
  def __init__(self, _visible):
    super().__init__(_visible)
    self.returnButton = Button(returnButton, "returnbutton.jpg")
    self.uiElements.append(self.returnButton)
    Menu.objects.append(self)
  def update(self):
    for uiElement in self.uiElements:
      uiElement.update()

class CreditsMenu(Menu):
  def __init__(self, _visible):
    super().__init__(_visible)
    self.returnButton = Button(returnButton, "returnbutton.png")
    self.uiElements.append(self.returnButton)
    Menu.objects.append(self)
  def update(self):
    DISPLAYSURF.fill((32,33,38))
    for uiElement in self.uiElements:
      uiElement.update()

def playButton():
  Menu.objects[0].visible = False
  Menu.objects[1].visible = True
  print("wow")

def quitButton():
  pygame.quit()
  sys.exit()

def returnButton():
  Menu.objects[1].visible = False
  Menu.objects[0].visible = True

MainMenu(True)
OtherMenu(False)
while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    DISPLAYSURF.fill(background_color)
    for menu in Menu.objects:
      if menu.visible:
        menu.update()
    pygame.display.update()

# Make an actual UI design that looks good
# Integrate my UI into the main code
# Make a pause/unpause system
# Figure out how to mute sound
# Coordinate with my team to make a shop menu
# Coordinate with my team to make an inventory system
# And the game is done!


# Victory Sound
# Defeat Sound
# Fire projectile sound
# 