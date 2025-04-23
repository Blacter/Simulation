from entity.entity import Entity
from coordinates import Coordinates


class Grass(Entity):
    def __init__(self, coordinates: Coordinates, hp: int) -> None:
        super().__init__(coordinates)
        self.__hp: int = hp    

    @property
    def hp(self) -> int:
        return self.__hp
    
    def __repr__(self) -> str:
        return f"Grass({super().__repr__()})"

    def be_eated(self, eat_damage: int):
        pass