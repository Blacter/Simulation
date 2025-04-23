MAP_HEIGHT: int = 5
MAP_WIDTH: int = 5

ROCK_RARITY: float = 0.0 # 0.05
TREE_RARITY: float = 0.0 # 0.05
GRASS_RARITY: float = 0.1 # 0.25

HERBIVORE_RARITY: float = 0.05 # 0.05
PREDATOR_RARITY: float = 0.05 # 0.02

GRASS_HP: int = 40
HERBIVORE_HP: int = 100
PREDATOR_HP: int = 100

HERBIVORE_SPEED: int = 1
PREDATOR_SPEED: int = 2

PREDATOR_DAMAGE: int = 60


class Settings: # TODO maybe better to devide class into few small classes like Rock_Settings, Predator_Settings etc.
    def __init__(self):
        self.__rock_rarity: float = ROCK_RARITY
        self.__tree_rarity: float = TREE_RARITY
        self.__grass_rarity: float = GRASS_RARITY
        self.__herbivore_rarity: float = HERBIVORE_RARITY
        self.__predator_rarity: float = PREDATOR_RARITY
        
        self.__grass_hp: int = GRASS_HP
        self.__herbivore_hp: int = HERBIVORE_HP
        self.__predator_hp: int = PREDATOR_HP
        
        self.__herbivore_speed: int = HERBIVORE_SPEED
        self.__predator_speed: int = PREDATOR_SPEED
        
        self.__predator_damage: int = PREDATOR_DAMAGE        
        
        self.__map_height: int = MAP_HEIGHT
        self.__map_width: int = MAP_WIDTH
        
    @property
    def rock_rarity(self) -> float:
        return self.__rock_rarity
    
    @property
    def tree_rarity(self) -> float:
        return self.__tree_rarity
    
    @property
    def grass_rarity(self) -> float:
        return self.__grass_rarity
    
    @property
    def herbivore_rarity(self) -> float:
        return self.__herbivore_rarity
    
    @property
    def predator_rarity(self) -> float:
        return self.__predator_rarity    
    
    @property
    def grass_hp(self) -> int:
        return self.__grass_hp
    
    @property
    def herbivore_hp(self) -> int:
        return self.__herbivore_hp
    
    @property
    def predator_hp(self) -> int:
        return self.__predator_hp
    
    @property
    def herbivore_speed(self) -> int:
        return self.__herbivore_speed
    
    @property
    def predator_speed(self) -> int:
        return self.__predator_speed
    
    @property
    def predator_damage(self) -> int:
        return self.__predator_damage
    
    @property
    def map_height(self) -> int:
        return self.__map_height
    
    @property
    def map_width(self) -> int:
        return self.__map_width
