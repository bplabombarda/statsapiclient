from statsapiclient.schedule import Schedule


class TestSchedule:
    def test_single_date(self):
        schedule = Schedule('01/01/2011')
        
        assert schedule.start_date == schedule.end_date

    def test_two_dates(self):
        schedule = Schedule('01/01/2011', '01/02/2011')
        
        assert schedule.start_date != schedule.end_date
