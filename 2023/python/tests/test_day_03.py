from src.solutions.day_03 import Solution


class TestDay03:
    def test_numbers_in_engine_schematic_are_recognized_and_summed(self):
        # GIVEN
        data = [
            "467..114..\n",
            "...*......\n",
            "..35..633.\n",
            "......#...\n",
            "617*......\n",
            ".....+.58.\n",
            "..592.....\n",
            "......755.\n",
            "...$.*....\n",
            ".664.598..\n",
        ]
        solution = Solution(data=data)
        # WHEN
        result = solution.part1()
        # THEN
        assert result == 4361


def test_part1():
    assert False
