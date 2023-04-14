import pygame
import entityHandler

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image_paths, x_speed, y_speed):
        super().__init__()
        self.image_paths = image_paths
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation_speed = 0.2
        self.current_time = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time > self.animation_speed:
            self.current_time -= self.animation_speed
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]

        self.rect.x += self.x_speed * dt
        self.rect.y += self.y_speed * dt

    def set_x_speed(self, x_speed):
        self.x_speed = x_speed

    def set_y_speed(self, y_speed):
        self.y_speed = y_speed

    def set_animation_speed(self, animation_speed):
        self.animation_speed = animation_speed