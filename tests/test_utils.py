from unittest import TestCase, mock
from unittest.mock import patch

import pytest
from requests import HTTPError

from statsapiclient.utils import fetch_html, fetch_json, validate_date


class TestFetchHtml(TestCase):
    @patch('statsapiclient.utils.get')
    def test_return_response(self, mock_get):
        mock_get.return_value.ok = True
        response = fetch_html(mock.ANY)

        self.assertIsNotNone(response)

    @patch('statsapiclient.utils.get')
    def test_return_error_response(self, mock_get):
        mock_get.return_value.ok = False
        response = fetch_html(mock.ANY)

        self.assertIsNotNone(response)

    @patch('statsapiclient.utils.get')
    def test_raise_exception(self, mock_get):
        exception = HTTPError(mock.Mock(status=404), "not found")
        mock_get(mock.ANY).raise_for_status.side_effect = exception

        with pytest.raises(HTTPError) as error_info:
            fetch_html("bad")
            self.assertEqual(error_info, exception)


class TestFetchJson(TestCase):
    @patch('statsapiclient.utils.get')
    def test_return_response(self, mock_get):
        mock_get.return_value.ok = True
        response = fetch_json(mock.ANY)

        self.assertIsNotNone(response)

    @patch('statsapiclient.utils.get')
    def test_return_error_response(self, mock_get):
        mock_get.return_value.ok = False
        response = fetch_json(mock.ANY)

        self.assertIsNotNone(response)

    @patch('statsapiclient.utils.get')
    def test_raise_exception(self, mock_get):
        exception = HTTPError(mock.Mock(status=404), "not found")
        mock_get(mock.ANY).raise_for_status.side_effect = exception

        with pytest.raises(HTTPError) as error_info:
            fetch_json("bad")
            self.assertEqual(error_info, exception)


class TestValidateDate(TestCase):
    def test_validate_date_valid(self):
        self.assertTrue(validate_date('1999-09-09'))

    def test_validate_date_invalid(self):
        with pytest.raises(ValueError) as excinfo:
            validate_date('09-09-1999')
        self.assertIn("Incorrect date format", str(excinfo.value))

    def test_validate_date_invalid_again(self):
        with pytest.raises(ValueError) as excinfo:
            validate_date('09/09/1999')
        self.assertIn("Incorrect date format", str(excinfo.value))

    def test_validate_date_invalid_againer(self):
        with pytest.raises(ValueError) as excinfo:
            validate_date('')
        self.assertIn("Incorrect date format", str(excinfo.value))
