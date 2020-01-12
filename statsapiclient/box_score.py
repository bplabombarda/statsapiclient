"""This class provides access to box score data
given a dict of game data."""
from dataclasses import dataclass


@dataclass
class BoxScore:
    """Dataclass to hold box score data.
    
    Parameters
    ----------

    data : dict
        A dictionary of box score data.

    
    TODO:
    This will be used to specify exactly which pieces
    of data under the `box score` section will be exposed.
    """
    data: dict
