import pygame
from sys import exit
from widget import Widget
from button import Button
from menu import Menu

def confirmQuitButton():
  pygame.quit()
  exit()

def deactivateConfirmationMenu():
    Menu.objects[3].visible = False

class ConfirmationMenu(Menu):
    def __init__(self, _visible, _parentUI):
        super().__init__(_visible, _parentUI)
        self.menubackground = Widget("zz_menu.png", self.parent, 750, 400)
        self.cancel = Button(deactivateConfirmationMenu, "zz_cancelbutton.png", self.parent, 780, 550)
        self.confirm = Button(confirmQuitButton, "zz_quitbutton2.png", self.parent, 780, 650)
        self.uiElements.append(self.menubackground)
        self.uiElements.append(self.cancel)
        self.uiElements.append(self.confirm)
        Menu.objects.append(self)
    def update(self):
        for uiElement in self.uiElements:
            uiElement.update()