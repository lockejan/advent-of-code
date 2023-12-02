import pytest
from day_01 import Calibrator


# test that a single number is extracted
# test that two numbers are extracted
# test that three and more numbers are extracted properly
@pytest.mark.parametrize("character_seq, expected_length", [
    ("Bo1b", 1),
    ("asd3ksgf9", 2),
    ("ninesixthree8six8", 2),
])
def test_digits_are_extracted(character_seq: str, expected_length: int):
    coordinates = Calibrator()
    result = coordinates._collect_digits(character_seq)
    assert len(result) == expected_length


# test that a number is created of the parsed chars
# .. two numbers
# ... more numbers result in a two digit number
@pytest.mark.parametrize("list_of_chars, expected_number", [
    (['5'], 55),
    (['4', '6'], 46),
    (['8', '3', '2'], 82),
])
def test_digits_are_converted_two_a_two_digit_number(list_of_chars: list[str],
                                                     expected_number: int):
    coordinates = Calibrator()
    result = coordinates._transform_to_int(list_of_chars)
    assert result is expected_number


# test that a list of numbers is reduced properly
def test_list_of_numbers_is_reduced():
    input = [11, 23, 53, 42, 00]
    coordinates = Calibrator(input)
    result = coordinates._reducer()
    assert result == 129
