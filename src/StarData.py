from dataclasses import dataclass


@dataclass(order=True)
class StarData:
    name: str
    right_ascension: float
    declination: float
    constellation: str
    Vmag: float