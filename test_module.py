# We start using TDD:
import pytest
from time_calculator import add_time


@pytest.fixture()
def input_valu():
    valu = ["3:00 PM", "3:10", "Monday", "11:30 AM", "2:32", "Monday", "11:43 AM", "00:20", "10:10 PM", "3:30", "11:43 "
                                                                                                                "PM",
            "24:20", "Tuesday", "6:30 PM", "205:12"]
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


# @pytest.mark.skip
def test_add_time_2(input_valu):
    assert add_time(input_valu[6], input_valu[7]) == "12 : 03 PM"


# @pytest.mark.skip
def test_add_time_3(input_valu):
    assert add_time(input_valu[8], input_valu[9]) == "1 : 40 AM (next day)"


# @pytest.mark.skip
def test_add_time_3_day(input_valu):
    assert add_time(input_valu[10], input_valu[11], input_valu[12]) == "12 : 03 AM, Tuesday (2 days later)"


# @pytest.mark.skip
def test_add_time_4(input_valu):
    assert add_time(input_valu[13], input_valu[14]) == "7 : 42 AM (9 days later)"
