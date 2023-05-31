from widget import Widget
from button import Button
from menu import Menu

class PauseMenu(Menu):
  def __init__(self, _visible, _parentUI):
    super().__init__(_visible, _parentUI)
    Menu.objects.append(self)
  def update(self):
    pass