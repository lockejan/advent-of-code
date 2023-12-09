import pytest

from src.solutions.day_01 import Solution


class TestClass:

    @pytest.mark.parametrize("character_seq, expected_length", [
        ("Bo1b", 1),
        ("asd3ksgf9", 2),
        ("ninesixthree8six8", 2),
    ])
    def test_digits_are_extracted_from_string(self, character_seq: str,
                                              expected_length: int):
        # GIVEN
        solution = Solution()
        # WHEN
        result = solution._collect_digits(character_seq)
        # THEN
        assert len(result) == expected_length

    @pytest.mark.parametrize("list_of_chars, expected_number", [
        (['5'], 55),
        (['4', '6'], 46),
        (['8', '3', '2'], 82),
    ])
    def test_digits_are_converted_into_a_two_digit_number(
            self, list_of_chars: list[str], expected_number: int):
        # GIVEN
        solution = Solution()
        # WHEN
        result = solution._transform_to_int(list_of_chars)
        # THEN
        assert result is expected_number

    def test_list_of_calibration_values_is_computed(self):
        input = [
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet',
        ]
        # GIVEN
        solution = Solution(data=input)
        # WHEN
        result = solution.part1()
        # THEN
        assert result == 142

    @pytest.mark.parametrize("char_seq, expected_number", [
        ("Boneoneb", 11),
        ("asdthreeksgfnine", 39),
        ("ninesixthree8six8", 98),
        ("eightwothree", 83),
    ])
    def test_written_number_is_transformed_into_a_number(
            self, char_seq: str, expected_number: int):
        # GIVEN
        solution = Solution()
        # WHEN
        result = solution._uniform_values_advanced(char_seq)
        # THEN
        assert result == expected_number

    @pytest.fixture
    def input_example(self):
        return [
            'eighthree',
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]

    def test_list_of_advanced_calibration_values_is_computed(self, input_example):
        # GIVEN
        solution = Solution(data=input_example)
        # WHEN
        result = solution.part2()
        # THEN
        assert result == (281 + 83)
