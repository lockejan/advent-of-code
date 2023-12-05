import pytest
from day_01 import Calibrator


@pytest.mark.parametrize("character_seq, expected_length", [
    ("Bo1b", 1),
    ("asd3ksgf9", 2),
    ("ninesixthree8six8", 2),
])
def test_digits_are_extracted_from_string(character_seq: str,
                                          expected_length: int):
    calibrator = Calibrator()
    result = calibrator._collect_digits(character_seq)
    assert len(result) == expected_length


@pytest.mark.parametrize("list_of_chars, expected_number", [
    (['5'], 55),
    (['4', '6'], 46),
    (['8', '3', '2'], 82),
])
def test_digits_are_converted_into_a_two_digit_number(list_of_chars: list[str],
                                                      expected_number: int):
    calibrator = Calibrator()
    result = calibrator._transform_to_int(list_of_chars)
    assert result is expected_number


def test_list_of_calibration_values_is_computed():
    input = [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet',
    ]
    calibrator = Calibrator(input)
    result = calibrator.compute_calibration()
    assert result == 142


@pytest.mark.parametrize("char_seq, expected_number", [
    ("Boneoneb", 11),
    ("asdthreeksgfnine", 39),
    ("ninesixthree8six8", 98),
    ("eightwothree", 83),
])
def test_written_number_is_transformed_into_a_number(char_seq: str,
                                                     expected_number: int):
    calibrator = Calibrator()
    result = calibrator._uniform_values_advanced(char_seq)
    assert result == expected_number


def test_list_of_calibration_advanced_values_is_computed():
    input = [
        'eighthree',
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen',
    ]
    calibrator = Calibrator(input)
    result = calibrator.compute_calibration_advanced()
    assert result == (281 + 83)
