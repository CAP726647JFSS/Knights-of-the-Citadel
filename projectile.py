import pygame
import math

class Projectile:
    def __init__(self, pos, vel, size, sprite, sprite_frames = []):
        self.pos = pos
        self.vel = vel
        self.size = size
        self.angle = 0
        self.sprite_frames = [sprite]
        self.sprite = sprite
        self.frame = 0
        self.animation_speed = 5  # Number of frames to wait before switching to next animation frame
        self.frame_counter = 0

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle = math.degrees(math.atan2(self.vel[1], self.vel[0]))
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame = (self.frame + 1) % len(self.sprite_frames)
            self.sprite = self.sprite_frames[self.frame]

    def draw(self, surface):
        rotated_surface = pygame.transform.rotate(pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA), -self.angle)
        sprite_rect = pygame.Rect(self.sprite.get_rect())
        sprite_rect.center = (self.size, self.size)
        rotated_surface.blit(self.sprite, sprite_rect)
        surface.blit(rotated_surface, (self.pos[0]-self.size, self.pos[1]-self.size))
