from unittest import mock
from unittest.mock import patch

import pytest
from requests import HTTPError

from statsapiclient.utils import fetch_html, fetch_json, validate_date


class TestFetchHtml:
    @patch('statsapiclient.utils.get')
    def test_return_response(self, mock_get):
        mock_get.return_value.ok = True
        response = fetch_html(mock.ANY)

        assert response is not None

    @patch('statsapiclient.utils.get')
    def test_return_error_response(self, mock_get):
        mock_get.return_value.ok = False
        response = fetch_html(mock.ANY)

        assert response is not None

    @patch('statsapiclient.utils.get')
    def test_raise_exception(self, mock_get):
        exception = HTTPError(mock.Mock(status=404), "not found")
        mock_get(mock.ANY).raise_for_status.side_effect = exception

        with pytest.raises(HTTPError) as error_info:
            fetch_html("bad")
            assert error_info == exception


class TestFetchJson:
    @patch('statsapiclient.utils.get')
    def test_return_response(self, mock_get):
        mock_get.return_value.ok = True
        response = fetch_json(mock.ANY)

        assert response is not None

    @patch('statsapiclient.utils.get')
    def test_return_error_response(self, mock_get):
        mock_get.return_value.ok = False
        response = fetch_json(mock.ANY)

        assert response is not None

    @patch('statsapiclient.utils.get')
    def test_raise_exception(self, mock_get):
        exception = HTTPError(mock.Mock(status=404), "not found")
        mock_get(mock.ANY).raise_for_status.side_effect = exception

        with pytest.raises(HTTPError) as error_info:
            fetch_json("bad")
            assert error_info == exception


class TestValidateDate:
    def test_validate_date_valid(self):
        assert validate_date('1999-09-09') is True

    def test_validate_date_invalid(self):
        with pytest.raises(ValueError) as excinfo:
            validate_date('09-09-1999')
        assert "Incorrect date format" in str(excinfo.value)

    def test_validate_date_invalid_again(self):
        with pytest.raises(ValueError) as excinfo:
            validate_date('09/09/1999')
        assert "Incorrect date format" in str(excinfo.value)

    def test_validate_date_invalid_againer(self):
        with pytest.raises(ValueError) as excinfo:
            validate_date('')
        assert "Incorrect date format" in str(excinfo.value)
