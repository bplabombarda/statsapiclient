from statsapiclient.games.summary import Summary

game_obj = {
    "liveData": {
        "boxscore": {},
        "linescore": {},
        "plays": {}
    }
}

mock_goals = [{
    "about": {
        "ordinalNum": "1st",
        "periodTimeRemaining": "19:59",
    },
    "result": {
        "description": "Somebody scored!",
        "eventTypeId": "GOAL",
        "strength": {
            "name": "Even",
        },
    },
    "team": {
        "triCode": "SEA",
    },
}]

mock_penalties = [{
    "about": {
        "ordinalNum": "1st",
        "periodTimeRemaining": "19:59",
    },
    "result": {
        "description": "Somebody did a bad!",
        "eventTypeId": "PENALTY",
        "secondaryType": "Bad thing",
        "penaltyMinutes": "2",
    },
    "team": {
        "triCode": "SEA",
    },
}]


class TestSummary:
    def test__filter_plays(self):
        game = Summary(mock_penalties, mock_goals)
        print(game)

        assert True

    def test__build_event_play_goal(self):
        game = Summary([], mock_goals)

        expected = {
            "period": "1st",
            "time": "19:59",
            "team": "SEA",
            "strength": "Even",
            "description": "Somebody scored!",
        }

        play = game.build_event_play(mock_goals[0])

        assert play == expected

    def test__build_event_play_penalty(self):
        game = Summary(mock_penalties, [])

        expected = {
            "period": "1st",
            "time": "19:59",
            "team": "SEA",
            "strength": "Bad thing (2 min)",
            "description": "Somebody did a bad!",
        }

        play = game.build_event_play(mock_penalties[0])

        assert play == expected
