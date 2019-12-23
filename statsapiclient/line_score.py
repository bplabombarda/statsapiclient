"""This class provides access to linescore data
given a dict of game data."""


class LineScore:
    """
    Gets linescore data.
    Args:
        :data: Raw linescore object
    """

    def __init__(self, data):
        self.current_period = data["currentPeriod"]
        self.current_period_display = data["currentPeriodOrdinal"]
        self.current_period_time_remaining = data["currentPeriodTimeRemaining"]
        self.is_at_intermission = data["intermissionInfo"]["isIntermission"]
        self.has_shootout = data["hasShootout"]
        self.power_play_strength = data["powerPlayStrength"]
