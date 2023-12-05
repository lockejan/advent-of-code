#!/usr/bin/env python

import re


class Calibrator:
    numbers: dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def __init__(self, calibration_data: list = None) -> None:
        if calibration_data is None:
            self.calibration_data = list()
        else:
            self.calibration_data = calibration_data

    @classmethod
    def with_file_input(cls, filename: str = None) -> 'Calibrator':
        if filename is None:
            return cls()
        with open(filename, 'r') as file:
            file_content = file.readlines()
        return cls(file_content)

    def _collect_digits(self, line: str) -> list:
        return [i for i in line.rstrip('\n') if i.isdigit()]

    def _transform_to_int(self, digits: list[str]) -> int:
        result = 0
        if len(digits) >= 2:
            result = ''.join(digits[::len(digits) - 1])
        if len(digits) < 2:
            result = ''.join(digits * 2)
        return int(result)

    def _uniform_values(self, line: str) -> int:
        digits = self._collect_digits(line)
        return self._transform_to_int(digits)

    def _text_to_numbers(self, text: str) -> str:
        pattern = re.compile(
            r'(?=(one|two|three|four|five|six|seven|eight|nine))')
        replacement = lambda match: str(Calibrator.numbers.get(match.group(1)))
        return re.sub(pattern, replacement, text)

    def _uniform_values_advanced(self, line: str) -> int:
        transformed_line = self._text_to_numbers(line)
        return self._uniform_values(transformed_line)

    def compute_calibration(self) -> int:
        result = list(map(self._uniform_values, self.calibration_data))
        return sum(result)

    def compute_calibration_advanced(self) -> int:
        result = list(map(self._uniform_values_advanced,
                          self.calibration_data))
        return sum(result)


if __name__ == '__main__':
    calibrator = Calibrator.with_file_input("../resources/input-1.txt")
    result_a = calibrator.compute_calibration()
    print(f"day_01-a: {result_a}")
    result_b = calibrator.compute_calibration_advanced()
    print(f"day_01-b: {result_b}")
