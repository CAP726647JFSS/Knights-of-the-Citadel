import pygame

class EntityHandler():
    def __init__(self, entity, max_health):
        self.entity = entity
        self.hitbox = entity.rect
        self.max_health = max_health
        self.current_health = max_health

    def update_hitbox(self):
        self.hitbox = self.entity.rect

    def get_hitbox(self):
        return self.hitbox

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.kill()

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def kill(self):
        self.entity.kill()

    def is_alive(self):
        return self.current_health > 0

class CollisionHandler():
    def __init__(self):
        self.entity_handlers = []

    def add_entity_handler(self, entity_handler):
        self.entity_handlers.append(entity_handler)

    def check_collisions(self):
        for i, entity_handler1 in enumerate(self.entity_handlers):
            for entity_handler2 in self.entity_handlers[i+1:]:
                if entity_handler1.get_hitbox().colliderect(entity_handler2.get_hitbox()):
                    self.handle_collision(entity_handler1, entity_handler2)

    def handle_collision(self, entity_handler1, entity_handler2):
        # Placeholder method - implement collision behavior here
        pass