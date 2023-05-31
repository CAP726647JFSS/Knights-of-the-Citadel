# https://www.youtube.com/watch?v=f29ZOu4rXlM
#https://www.google.com/search?q=menu+buttons&tbm=isch&ved=2ahUKEwj0ybXw1ov_AhUXElkFHSTqBxsQ2-cCegQIABAA&oq=menu+buttons&gs_lcp=CgNpbWcQAzIHCAAQigUQQzIHCAAQigUQQzIHCAAQigUQQzIFCAAQgAQyBwgAEIoFEEMyBwgAEIoFEEMyBQgAEIAEMgcIABCKBRBDMgcIABCKBRBDMgUIABCABFDjFVjjFWCmF2gAcAB4AIABhwGIAYcBkgEDMC4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=ZNFsZPSHBZek5NoPpNSf2AE&bih=1032&biw=1903&rlz=1C1GCEA_enCA1059&safe=active&hl=en-US#imgrc=0-hfIaHGGSk1JM
#https://www.youtube.com/watch?v=wkrXbl1RlAg&ab_channel=FHCoding


import pygame, sys
from pygame.locals import QUIT
from confirmationmenu import ConfirmationMenu
from creditsmenu import CreditsMenu
from mainmenu import MainMenu
from pausemenu import PauseMenu
from shopmenu import ShopMenu
from settingsmenu import SettingsMenu
from menu import Menu

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Knights of the Citadel!')

MainMenu(True, DISPLAYSURF) # Pos 0
SettingsMenu(False, DISPLAYSURF) # Pos 1
CreditsMenu(False, DISPLAYSURF) # Pos 2
ConfirmationMenu(False, DISPLAYSURF) # Pos 3
ShopMenu(False, DISPLAYSURF) # Pos 4
PauseMenu(False, DISPLAYSURF) # Pos 5
background_image = pygame.image.load("zz_background.png")
game_logo = pygame.image.load("zz_logo.png")
while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    DISPLAYSURF.blit(background_image, (0,0))
    DISPLAYSURF.blit(game_logo, (1770,0))
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