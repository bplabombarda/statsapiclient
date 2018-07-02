from statsapiclient import Client


class Schedule(Client):
	_endpoint = 'api/v1/schedule'
	params={
		'expand': 'schedule.teams,schedule.linescore,schedule.decisions,schedule.scoringplays'
		}

	def __init__(self):
		return

	def _handle_dates(self, response):
		return response['dates']

	def games_from_date(self, date):
		self.params['startDate'] = date
		self.params['endDate'] = date
		
		response = self.fetch(self._endpoint, params=self.params)
		return self._handle_dates(response)

	def games_from_date_range(self, start_date, end_date):
		self.params['startDate'] = start_date
		self.params['endDate'] = end_date
		
		response = self.fetch(self._endpoint, params=self.params)
		return self._handle_dates(response)

