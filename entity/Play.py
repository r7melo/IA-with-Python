from entity.base.Entity import Entity

class Play(Entity):
    def __init__(self, source=None, root=None) -> None:
        super().__init__(source, root)

    def update(self) -> None:
        self.root.x += 1