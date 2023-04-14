import pygame

class Button:
  objects = [] # Variable for keeping track of the amount of instances of 'Button' there is
  def __init__(self, x, y, width, height, buttonText, onClick):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.buttonText = buttonText
    self.onClick = onClick
    self.pressed = False
    self.buttonColors = {
      'normal': (100,100,100),
      'hover': (150,150,150),
      'pressed': (50,50,50)
    }
    self.buttonSurf = pygame.font.SysFont('Times New Roman', 40).render(self.buttonText, True, (20, 20, 20))
    Button.objects.append(self)

  def update(self):
    buttonSurface = pygame.Surface((self.width, self.height))
    buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
    buttonSurface.fill(self.buttonColors['normal'])
    buttonSurface.blit(self.buttonSurf, (175, 0))
    mousePos = pygame.mouse.get_pos()
    if buttonRect.collidepoint(mousePos):
      #print("Hover")
      buttonSurface.fill(self.buttonColors['hover'])
      buttonSurface.blit(self.buttonSurf, (175, 0))
      if pygame.mouse.get_pressed(num_buttons=3)[0] and not self.pressed:
        buttonSurface.fill(self.buttonColors['pressed'])
        self.onClick()
        self.pressed = True
      elif not pygame.mouse.get_pressed(num_buttons=3)[0] and self.pressed:
        self.pressed = False
    screen.blit(buttonSurface, (self.x, self.y)) # Project all on the screen