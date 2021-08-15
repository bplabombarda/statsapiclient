"""This dataclass holds all play data and contains the methods
to get and section said data.
"""
from dataclasses import dataclass


@dataclass
class Play:
    """This is where the play data happens.

    Parameters
    ----------
    all_plays : list
        List of play dictionaries.

    current_play : dict
        Current play dictionary.

    penalty_indicies : list
        List of indicies of penalty plays.

    scoring_indicies : list
        List of indicies of scoring plays.

    play_indicies_by_period : dict
        Dictionay of period dicts containing plays and start and end indicies.
    """
    all_plays: list
    current_play: dict
    penalty_indicies: list
    scoring_indicies: list
    play_indicies_by_period: dict

    def get_plays_by_period(self, period):
        """Get plays by period.

        Parameters
        ----------
        period : int
            Integer representation of the period.
            One of 1, 2, 3, or 4 (for overtime).

        Returns
        -------
        list
            A filtered list of all plays whose indicies appear in the
            periods play index range.
        """
        def filter_by_period(play):
            """Helper function to pass to the filter."""
            play_index = play["about"]["eventIdx"]
            period_plays = self.play_indicies_by_period[period]
            start_index = period_plays["startIndex"]
            end_index = period_plays["endIndex"]

            return start_index <= play_index <= end_index

        if period not in (1, 2, 3, 4):
            raise ValueError("Period value should be 1, 2, 3, or 4")

        plays_in_period = list(filter(filter_by_period, self.all_plays))

        return plays_in_period

    def get_penalty_plays(self):
        """Gets a list of penalty plays.

        Returns
        -------
        list
            A filtered list of all plays whose indicies appear in the
            penalty_indicies list.
        """

        def filter_penalties(play):
            """Helper function to filter penalty plays."""
            return play["about"]["eventIdx"] in self.penalty_indicies

        penalty_plays = list(filter(filter_penalties, self.all_plays))

        return penalty_plays

    def get_scoring_plays(self):
        """Gets a list of scoring plays.

        Returns
        -------
        list
            A filtered list of all plays whose indicies appear in the
            scoring_indicies list.
        """

        def filter_scoring(play):
            """Helper function to filter scoring plays."""
            return play["about"]["eventIdx"] in self.scoring_indicies

        scoring_plays = list(filter(filter_scoring, self.all_plays))

        return scoring_plays
