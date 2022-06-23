class Entity:
    def __init__(self, source=None, root=None, draw=True) -> None:
        self.source = source
        self.root = root
        self.draw = draw

    def update(self) -> None:
        pass