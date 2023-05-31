class Menu:
    objects = []
    def __init__(self, _visible, _parentUI):
        self.visible = _visible
        self.parent = _parentUI
        self.uiElements = []
    def activateMenu(self):
        self.visible = True
    def deactivateMenu(self):
        self.visible = False