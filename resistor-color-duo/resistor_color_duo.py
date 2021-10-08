from enum import Enum
from typing import List

Colors = List[str]


class Resistors(Enum):

    BLACK = 0
    BROWN = 1
    RED = 2
    ORANGE = 3
    YELLOW = 4
    GREEN = 5
    BLUE = 6
    VIOLET = 7
    GREY = 8
    WHITE = 9


def value(colors: Colors) -> int:

    band_1, band_2 = [c.upper() for c in colors]
    return int(10 * Resistors[band_1].value + Resistors[band_2].value)