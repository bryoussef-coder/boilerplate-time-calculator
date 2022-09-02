# We start using TDD:
import pytest
from time_calculator import add_time


@pytest.fixture()
def input_valu():
    valu = ["3:00 PM", "3:10", "Monday", "11:30 AM", "2:32", "Monday", "11:43 AM", "00:20"]
    return valu


# @pytest.mark.skip
def test_add_time_1(input_valu):
    assert add_time(input_valu[0], input_valu[1]) == "6 : 10 PM"


# @pytest.mark.skip
def test_add_time_1_day(input_valu):
    assert add_time(input_valu[0], input_valu[1], input_valu[2]) == "6 : 10 PM, Monday"


# @pytest.mark.skip
def test_add_time_2_day(input_valu):
    assert add_time(input_valu[3], input_valu[4], input_valu[5]) == "2 : 02 PM, Monday"


#@pytest.mark.skip
def test_add_time_2(input_valu):
    assert add_time(input_valu[6], input_valu[7]) == "12 : 03 PM"
