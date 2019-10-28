import pytest

from statsapiclient.schedule import Schedule
# from tests.mocks.schedule_mock import dates

dates = [{
    "games": [
        {"gamePk": 1},
        {"gamePk": 2},
    ]
}, {
    "games": [
        {"gamePk": 3},
        {"gamePk": 4},
    ]
}]


class TestSchedule:
    def test_single_date(self):
        schedule = Schedule('2011-01-01')

        assert schedule.params["startDate"] == schedule.params["endDate"]

    def test_date_range(self):
        schedule = Schedule('2011-01-01', '2011-01-02')

        assert schedule.params["startDate"] != schedule.params["endDate"]

    def test_single_date_get_games(self):
        schedule = Schedule('2011-01-01')
        schedule.data = [dates[0]]

        games = schedule.get_games()

        assert len(games) == 2

    def test_multiple_dates_get_games(self):
        schedule = Schedule('2011-01-01', '2011-01-02')
        schedule.data = dates

        games = schedule.get_games()

        assert len(games) == 4

    def test_validate_date_valid(self):
        assert Schedule.validate_date('1999-09-09')

    def test_validate_date_invalid(self):
        with pytest.raises(ValueError) as excinfo:
            Schedule.validate_date('09-09-1999')
        assert "Incorrect data format" in str(excinfo.value)

    def test_validate_date_invalid_again(self):
        with pytest.raises(ValueError) as excinfo:
            Schedule.validate_date('09/09/1999')
        assert "Incorrect data format" in str(excinfo.value)

    def test_validate_date_invalid_againer(self):
        with pytest.raises(ValueError) as excinfo:
            Schedule.validate_date('')
        assert "Incorrect data format" in str(excinfo.value)
