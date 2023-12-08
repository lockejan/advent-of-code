#!/usr/bin/env python

from src.solutions.day_01 import Solution as Solution01
from src.solutions.day_02 import Solution as Solution02


def main():
    solution01 = Solution01.with_file_input("../resources/input-1.txt")
    print(f"day_01-a: {solution01.part1()}")
    print(f"day_01-b: {solution01.part2()}")

    solution02 = Solution02.with_file_input("../resources/input-2.txt")
    print(f"day_02-a: {solution02.part1()}")
    print(f"day_02-b: {solution02.part2()}")


if __name__ == '__main__':
    main()
