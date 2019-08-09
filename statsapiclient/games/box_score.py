class BoxScore:
    """
    Gets boxscore data.
    Args:
        :data: Raw boxscore object
    """

    def __init__(self, data):
        self.data = data

    # Game data methods
    def get_current_period(self):
        return self.data["currentPeriod"]

    def get_current_period_ordinal(self):
        return self.data["currentPeriodOrdinal"]

    def get_time_remaining_in_period(self):
        return self.data["currentPeriodTimeRemaining"]

    def is_at_intermission(self):
        return self.data["intermissionInfo"]["intermission"]

    def get_power_play_strength(self):
        return self.data["powerPlayStrength"]

    # Score & shots on goal methods
    def get_score(self):
        return {
            "away": self.data["teams"]["away"]["goals"],
            "home": self.data["teams"]["home"]["goals"],
        }

    def get_shots_on_goal(self):
        return {
            "away": self.data["teams"]["away"]["shotsOnGoal"],
            "home": self.data["teams"]["home"]["shotsOnGoal"],
        }
