class LineScore:
    """
    Gets linescore data.
    Args:
        :data: Raw linescore object
    """

    def __init__(self, data):
        self.data = data

    # Game data methods
    def get_current_period(self):
        """Returns current period in numerical format."""
        return self.data["currentPeriod"]

    def get_current_period_ordinal(self):
        """Returns current period in ordinal format."""
        return self.data["currentPeriodOrdinal"]

    def get_time_remaining_in_period(self):
        """Returns time remaining in current period."""
        return self.data["currentPeriodTimeRemaining"]

    def is_at_intermission(self):
        """Returns boolean representing whether the game is currently
        at intermission or not.
        """
        return self.data["intermissionInfo"]["intermission"]

    def get_power_play_strength(self):
        """Returns current powerplay strngth, if any.""" 
        return self.data["powerPlayStrength"]

    # Score & shots on goal methods
    def get_score(self):
        """Returns a dict of scores keyed by 'away' and 'home'.""" 
        return {
            "away": self.data["teams"]["away"]["goals"],
            "home": self.data["teams"]["home"]["goals"],
        }

    def get_shots_on_goal(self):
        """Returns a dict of shots on goal keyed by 'away' and 'home'."""
        return {
            "away": self.data["teams"]["away"]["shotsOnGoal"],
            "home": self.data["teams"]["home"]["shotsOnGoal"],
        }
