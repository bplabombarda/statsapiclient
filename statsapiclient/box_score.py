"""This class provides access to box score data
given a dict of game data."""
from dataclasses import dataclass


@dataclass
class BoxScore:
    """Dataclass to hold box score data."""
    data: dict
