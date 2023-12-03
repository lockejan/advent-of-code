#!/usr/bin/env python


class Calibrator:

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

    def compute_calibration(self) -> int:
        result = list(map(self._uniform_values, self.calibration_data))
        return sum(result)


if __name__ == '__main__':
    calibrator = Calibrator.with_file_input("../resources/input-1.txt")
    result_a = calibrator.compute_calibration()
    print(f"day_01-a: {result_a}")
