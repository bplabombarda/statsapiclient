class Summary:
    def __init__(self, penalty_plays, scoring_plays):
        self.build_summary(penalty_plays, scoring_plays)

    def build_event_play(self, play):
        """Create a play dict for game summary.
        Args:
            :play: A play dict from raw play-by-play data.
        """
        strength = ""

        if play["result"]["eventTypeId"] == "GOAL":
            strength = play["result"]["strength"]["name"]

        if play["result"]["eventTypeId"] == "PENALTY":
            penalty = play["result"]["secondaryType"]
            minutes = play["result"]["penaltyMinutes"]
            strength = f"{penalty} ({minutes} min)"

        return {
            "period": play["about"]["ordinalNum"],
            "time": play["about"]["periodTimeRemaining"],
            "team": play["team"]["triCode"],
            "strength": strength,
            "description": play["result"]["description"],
        }

    def build_summary(self, penalty_plays, scoring_plays):
        """Build summary data dict."""
        penalty_plays = list(map(
            self.build_event_play,
            penalty_plays
        ))
        scoring_plays = list(map(
            self.build_event_play,
            scoring_plays
        ))

        self.game_summary = {
            "penalty_plays": penalty_plays,
            "scoring_plays": scoring_plays,
        }
