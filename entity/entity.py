from abc import ABC, abstractmethod

from coordinates import Coordinates


class Entity:
    def __init__(self, coordinates: Coordinates) -> None:
        self.coordinates = coordinates

    def __repr__(self):
        return str(self.coordinates)
