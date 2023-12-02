#!/usr/bin/env python

from functools import reduce


class Calibrator:

    def __init__(self, coordinates: list = list()) -> None:
        self.coordinates = coordinates

    def _get_lines_from_file(self, filename: str) -> list:
        file = open(filename, 'r')
        return file.readlines()

    def _collect_digits(self, line: str) -> list:
        return [i for i in line.rstrip('\n') if i.isdigit()]

    def _transform_to_int(self, digits: list[str]) -> int:
        result = 0
        if len(digits) >= 2:
            result = ''.join(digits[::len(digits) - 1])
        if len(digits) < 2:
            result = ''.join(digits * 2)
        return int(result)

    def _reducer(self) -> int:
        return reduce(lambda a, b: a + b, self.coordinates)

    def _prepare_coordinates(self, line: str) -> None:
        digits = self._collect_digits(line)
        result = self._transform_to_int(digits)
        self.coordinates.append(result)

    def compute_calibration(self, filename: str) -> int:
        for line in self._get_lines_from_file(filename):
            self._prepare_coordinates(line)
        return self._reducer()


if __name__ == '__main__':
    calibrator = Calibrator()
    result = calibrator.compute_calibration("../resources/input-1.txt")
    print(f"day_01-a: {result}")
