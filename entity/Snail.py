from entity.base.Entity import Entity

class Snail(Entity):
    def __init__(self, source=None, root=None) -> None:
        super().__init__(source, root)

    def update(self) -> None:
        self.root.x += -4

        if self.root.right <= 0:
            self.root.x = 800