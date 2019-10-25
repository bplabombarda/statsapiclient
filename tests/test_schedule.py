from statsapiclient.schedule import Schedule
# from tests.mocks.schedule_mock import dates

dates = [{
    "games": [
        {"gamePk": 1,},
        {"gamePk": 2,},
    ]
},{
    "games": [
        {"gamePk": 3,},
        {"gamePk": 4,},
    ]
}]


class TestSchedule:
    def test_single_date(self):
        schedule = Schedule('2011-01-01')

        assert schedule.params["startDate"] == schedule.params["endDate"]

    def test_date_range(self):
        schedule = Schedule('2011-01-01', '2011-01-02')
        
        assert schedule.params["startDate"] != schedule.params["endDate"]

    def test_single_date_games(self):
        schedule = Schedule('2011-01-01')
        schedule.data = [dates[0]]

        games = schedule.get_games()
    
        assert len(games) == 2

    def test_multiple_dates_games(self):
        schedule = Schedule('2011-01-01', '2011-01-02')
        schedule.data = dates

        games = schedule.get_games()
    
        assert len(games) == 4
