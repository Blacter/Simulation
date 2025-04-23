class Coordinates:
    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, coordinates):
        return self.x == coordinates.x and self.y == coordinates.y

    def __repr__(self) -> str:
        return 'Coordinates' + str((self.x, self.y))