from entity.entity import Entity
from coordinates import Coordinates

class Tree(Entity):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)

    def __repr__(self) -> str:
        return f"Tree({super().__repr__()})"