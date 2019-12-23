"""This class provides access to line score data
given a dict of game data."""
from dataclasses import dataclass


@dataclass
class LineScore:
    """Dataclass to hold line score data."""
    current_period: int
    current_period_display: str
    current_period_time_remaining: str
    has_shootout: bool
    is_at_intermission: bool
    power_play_strength: str
