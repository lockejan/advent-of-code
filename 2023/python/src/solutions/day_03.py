from src.utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def parse(self):
        # register position of numbers
        # but only those that are connected
        # to a symbol within the next position
        # lines before and after are allowed
        for line, column in enumerate(self.data):
            print(line, column)

    def part1(self):
        # first and last line only evolve around 2 lines.
        # make slices of three lines
        #
        # get range index of numbers
        # get index of symbols
        # recognize numbers with adjacent symbols changing row [-1,+1]
        # and column index [+1,-1]
        # 1.same line, 2.above, 3.beyond?
        # sum all found numbers
        # sliding window???
        self.parse()

    def part2(self):
        pass
