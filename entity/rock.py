from entity.entity import Entity
from coordinates import Coordinates

class Rock(Entity):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)

    def __repr__(self) -> str:
        return f"Rock({super().__repr__()})"