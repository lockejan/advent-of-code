import pytest

from src.solutions.day_02 import Solution


class TestClass:
    @pytest.fixture
    def game_data(self):
        return [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n",
            "Game 6: 6 red, 1 blue, 14 green; 2 blue, 1 red, 2 green\n",
            "Game 7: 6 red, 1 blue, 23 green; 15 blue, 1 red, 2 green\n",
            "Game 8: 6 red, 1 blue, 23 green; 2 blue, 13 red, 2 green\n",
        ]

    def test_game_can_be_parsed(self, game_data):
        # GIVEN
        expected = {"1": {"blue": 6, "red": 4, "green": 2}}
        solution = Solution()
        # WHEN
        actual = solution._parse(game_data[0])
        # THEN
        assert actual == expected

    def test_possibles_games_are_recognized_and_summed_by_game_id(self, game_data):
        # GIVEN
        solution = Solution(data=game_data)
        # WHEN
        actual = solution.part1()
        # THEN
        assert actual == 8

    def test_day_2_logic_is_computed_correctly(self):
        # GIVEN
        input_data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n",
        ]
        solution = Solution(data=input_data)
        # WHEN
        actual = solution.part2()
        # THEN
        assert actual == 2286
