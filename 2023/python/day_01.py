#!/usr/bin/env python

import re
from input_handler import InputHandler


class Calibrator(InputHandler):
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

    def _collect_digits(self, line: str) -> list:
        return [i for i in line.rstrip('\n') if i.isdigit()]

    def _transform_to_int(self, digits: list[str]) -> int:
        if len(digits) >= 2:
            return int(''.join(digits[::len(digits) - 1]))

        return int(''.join(digits * 2))

    def _uniform_values(self, line: str) -> int:
        digits = self._collect_digits(line)
        return self._transform_to_int(digits)

    def _text_to_numbers(self, text: str) -> str:
        pattern = re.compile(
            r'(?=(one|two|three|four|five|six|seven|eight|nine))')
        replacement = lambda match: str(self.numbers.get(match.group(1)))
        return re.sub(pattern, replacement, text)

    def _uniform_values_advanced(self, line: str) -> int:
        transformed_line = self._text_to_numbers(line)
        return self._uniform_values(transformed_line)

    def compute_calibration(self) -> int:
        return sum(list(map(self._uniform_values, self.data)))

    def compute_calibration_advanced(self) -> int:
        return sum(list(map(self._uniform_values_advanced, self.data)))


if __name__ == '__main__':
    calibrator = Calibrator.with_file_input("../resources/input-1.txt")
    print(f"day_01-a: {calibrator.compute_calibration()}")
    print(f"day_01-b: {calibrator.compute_calibration_advanced()}")
