from widget import Widget
from button import Button
from menu import Menu

def returnButton():
  Menu.objects[1].visible = False
  Menu.objects[0].visible = True

class CreditsMenu(Menu):
  def __init__(self, _visible, _parentUI):
    super().__init__(_visible, _parentUI)
    self.returnButton = Button(returnButton, "zz_returnbutton.png", self.parent)
    self.uiElements.append(self.returnButton)
    Menu.objects.append(self)
  def update(self):
    self.parent.fill((32,33,38))
    for uiElement in self.uiElements:
      uiElement.update()