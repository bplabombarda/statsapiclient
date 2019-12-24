import pytest

from statsapiclient.utils import validate_date


class TestUtils:
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
