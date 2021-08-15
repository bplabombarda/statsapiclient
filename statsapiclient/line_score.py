"""This class provides access to line score data
given a dict of game data."""
from dataclasses import dataclass


@dataclass
class LineScore:
    """Dataclass to hold line score data.

    Parameters
    ----------

    current_period : int
        Integer representation of the current period. Values include
        1, 2, 3, and 4 for overtime.

    current_period_display : str
        String representation of the current period.

    current_period_time_remainind : str
        String representation of the time remaining in
        the current period.

    has_shootout : book
        True if the game has or had a shootout. False if not.

    is_at_intermission : bool
        True if the game is at intermission. False if not.

    power_play_strength : str
        String representation of current power play strength.
    """
    current_period: int
    current_period_display: str
    current_period_time_remaining: str
    has_shootout: bool
    is_at_intermission: bool
    power_play_strength: str
