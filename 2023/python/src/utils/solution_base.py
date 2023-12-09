import timeit

from src.utils.input_handler import InputHandler


class SolutionBase(InputHandler):
    def __init__(self, day_num: int = -1, benchmark: bool = False, data: list = None):
        super().__init__(data)
        self.day_num = day_num
        self._benchmark = benchmark
        self.benchmark_times = []

    def solve(self, part_num: int) -> int:
        self.data = self.with_file_input(self.build_filepath_for_day(self.day_num))
        func = getattr(self, f"part{part_num}")
        self.benchmark()
        result = func()
        self.benchmark()
        return result

    def benchmark(self, _print=False) -> None:
        if _print and len(self.benchmark_times) > 0 and len(self.benchmark_times) % 2 == 0:
            t = self.benchmark_times[-1] - self.benchmark_times[-2]
            units = ["s", "ms", "µs", "ns"]
            unit_idx = 0
            while t < 1:
                t *= 1000
                unit_idx += 1
            print(f"benchmarking: {t:.2f} {units[unit_idx]}")
        elif self._benchmark:
            self.benchmark_times.append(timeit.default_timer())
