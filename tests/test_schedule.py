from statsapiclient.schedule import Schedule


class TestSchedule:
    def test_single_date(self):
        schedule = Schedule('01/01/2011')
        print(schedule.params)
        assert schedule.params["startDate"] == schedule.params["endDate"]

    def test_two_dates(self):
        schedule = Schedule('01/01/2011', '01/02/2011')
        
        assert schedule.params["startDate"] != schedule.params["endDate"]
