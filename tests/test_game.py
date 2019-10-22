from statsapiclient.games.game import Game

game_obj = {
    "liveData": {
        "boxscore": {},
        "linescore": {},
        "plays": {}
    }
}


class TestGame:
    def test__filter_plays(self):
        game = Game('1234567890')

        assert True

    def test__build_event_play_goal(self):
        game = Game('1234567890')
        mock_play = {
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
        }

        expected = {
            "period": "1st",
            "time": "19:59",
            "team": "SEA",
            "strength": "Even",
            "description": "Somebody scored!",
        }

        play = game._build_event_play(mock_play)

        assert play == expected

    def test__build_event_play_penalty(self):
        game = Game('1234567890')
        mock_play = {
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
        }

        expected = {
            "period": "1st",
            "time": "19:59",
            "team": "SEA",
            "strength": "Bad thing (2 min)",
            "description": "Somebody did a bad!",
        }

        play = game._build_event_play(mock_play)

        assert play == expected
    