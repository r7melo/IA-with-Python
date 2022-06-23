from entity.base.Entity import Entity
import pygame

class Play(Entity):
    def __init__(self, source=None, root=None) -> None:
        super().__init__(source, root)
        self.vector = pygame.Vector2(0,0)
        self.friction = 0.3
        self.max_friction = 4

        self.action = lambda: None


    def update(self) -> None:
        self.root.x += self.vector.x
        self.root.y += self.vector.y
        self.action()
        

    def keyboard(self, event) -> None:

        if pygame.key.get_pressed()[pygame.K_a]:
            self.action = self.mov_left
        
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.action = self.mov_rigth

        else:
            self.action = self.mov_stop

    def mov_left(self):
        self.vector.x = -4

    def mov_rigth(self):
        self.vector.x = 4

    def mov_stop(self):
        self.vector.x = 0

