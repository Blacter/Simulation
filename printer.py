DEFAULT_CONSOLE_STYLE: str = '\x1b[0;30;40m' #  \x1b[0;31;40m

GRASS_CONSOLE_STYLE: str = '\x1b[0;36;42m'
ROCK_CONSOLE_STYLE: str = '\x1b[0;31;47m' # \x1b[0;31;40m
TREE_CONSOLE_STYLE: str = '\x1b[0;33;46m'

GRASS_SPRITE: str = GRASS_CONSOLE_STYLE + ' # ' + DEFAULT_CONSOLE_STYLE
ROCK_SPRITE: str = ROCK_CONSOLE_STYLE + '^Ʌ^' + DEFAULT_CONSOLE_STYLE
TREE_SPRITE: str = TREE_CONSOLE_STYLE + ' Ѱ ' + DEFAULT_CONSOLE_STYLE
HERBIVORE_SPRITE: str = '_@_'
PREDATOR_SPRITE: str = '/*\\'

EMPTY_SQUARE_SPRITE_WHITE: str = '   '
EMPTY_SQUARE_SPRITE_BLUE: str = '\x1b[44m   ' + DEFAULT_CONSOLE_STYLE

class Sprites:
    def __init__(self):
        self.__default_console_style: str = DEFAULT_CONSOLE_STYLE
        
        self.__grass_console_style: str = GRASS_CONSOLE_STYLE
        self.__rock_console_style: str = ROCK_CONSOLE_STYLE
        self.__tree_console_style: str = TREE_CONSOLE_STYLE
        
        self.__grass_sprite: str = GRASS_SPRITE
        self.__rock_sprite: str = ROCK_SPRITE
        self.__tree_sprite: str = TREE_SPRITE
        self.__herbivore_sprite: str = HERBIVORE_SPRITE
        self.__predator_sprite: str = PREDATOR_SPRITE
        self.__empty_square_sprite_one: str = EMPTY_SQUARE_SPRITE_WHITE
        self.__empty_square_sprite_two: str = EMPTY_SQUARE_SPRITE_BLUE
    
    @property
    def default_console_style(self) -> str:
        return self.__default_console_style
    
    @property
    def grass_console_style(self) -> str:
        return self.__grass_console_style
    
    @property
    def rock_console_style(self) -> str:
        return self.__rock_console_style
    
    @property
    def tree_console_style(self) -> str:
        return self.__tree_console_style
    
    @property
    def grass_sprite(self) -> str:
        return self.__grass_sprite
    
    @property
    def rock_sprite(self) -> str:
        return self.__rock_sprite
    
    @property
    def tree_sprite(self) -> str:
        return self.__tree_sprite
    
    @property
    def herbivore_sprite(self) -> str:
        return self.__herbivore_sprite
    
    @property
    def predator_sprite(self) -> str:
        return self.__predator_sprite
    
    @property
    def empty_square_sprite(self) -> str:
        return self.__empty_square_sprite
    
    @property
    def empty_square_sprite_one(self) -> str:
        return self.__empty_square_sprite_one

    @property
    def empty_square_sprite_two(self) -> str:
        return self.__empty_square_sprite_two


    
    