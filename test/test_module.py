import pytest


@pytest.fixture()
def input_value():
    input = "3:55 PM"
    return input


def test_time_format(input_value) -> None:
    val = input_value.split()

    print(val)
