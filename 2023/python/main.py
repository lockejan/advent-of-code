#!/usr/bin/env python
import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(description="Advent of Code solution runner")
    parser.add_argument("-d", "--day", dest="day", metavar="day_number", type=int,
                        help="Required, day number of the AoC event", required=True)
    parser.add_argument("-p", "--part", dest="part", default=1, metavar="part_number", type=int,
                        help="Required, part number of the day of the AoC event")
    parser.add_argument("-b", "--benchmark", action="store_true", help="Optional, benchmarking the code")
    args = parser.parse_args()

    if not 0 < args.day < 26:
        print("day number must be between 1 and 25")
        exit()
    elif args.part not in [1, 2]:
        print("part number must be 1 or 2")
        exit()
    else:
        day_num = '0' + str(args.day) if args.day < 10 else args.day
        print(f"Solving day {args.day} part {args.part}\n")
        solution = importlib.import_module(f"src.solutions.day_{day_num}").Solution(
            args.day, args.benchmark)
        print(f"the answer is {answer}\n" if (answer := solution.solve(
            part_num=args.part)) is not None else "")
        solution.benchmark(_print=True)


if __name__ == '__main__':
    main()
