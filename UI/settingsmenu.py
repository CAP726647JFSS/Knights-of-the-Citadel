from widget import Widget
from button import Button
from menu import Menu

def returnButton():
  Menu.objects[1].visible = False
  Menu.objects[0].visible = True

class SettingsMenu(Menu):
  def __init__(self, _visible, _parentUI):
    super().__init__(_visible, _parentUI)
    self.returnButton = Button(returnButton, "zz_returnbutton.jpg", self.parent)
    self.uiElements.append(self.returnButton)
    Menu.objects.append(self)
  def update(self):
    for uiElement in self.uiElements:
      uiElement.update()