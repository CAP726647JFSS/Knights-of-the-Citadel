from widget import Widget
from button import Button
from menu import Menu

def playButton():
  Menu.objects[0].visible = False
  Menu.objects[1].visible = True
  print("wow")

def activateConfirmationMenu():
    Menu.objects[3].visible = True

class MainMenu(Menu):
  def __init__(self, _visible, _parentUI):
    super().__init__(_visible, _parentUI)
    self.menuBackground = Widget("zz_menubackground.png", self.parent, 100, -50)
    self.play = Button(playButton, "zz_playbutton2.png", self.parent, 230, 160)
    self.settings = Button(playButton, "zz_settingsbutton2.png", self.parent, 230, 260)
    self.credits = Button(playButton, "zz_creditsbutton2.png", self.parent, 230, 360)
    self.quit = Button(activateConfirmationMenu, "zz_quitbutton2.png", self.parent, 230, 460)
    self.uiElements.append(self.menuBackground)
    self.uiElements.append(self.play)
    self.uiElements.append(self.settings)
    self.uiElements.append(self.credits)
    self.uiElements.append(self.quit)
    Menu.objects.append(self)
  def update(self):
    for uiElement in self.uiElements:
      uiElement.update()