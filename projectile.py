import pygame

class Projectile:
    def __init__(self, pos, vel, size):
        self.pos = pos
        self.vel = vel
        self.size = size

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), self.size)