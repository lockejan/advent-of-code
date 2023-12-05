from day_02 import Guesser


class TestClass:

    def test_game_can_be_parsed(self):
        data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"]
        expected_result = {'1': {"blue": 6, "red": 4, "green": 2}}
        guesser = Guesser()
        result = guesser.parse_game(data[0])
        assert expected_result == result

    def test_possibles_games_are_recognized_and_summed_by_game_id(self):
        data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n",
            "Game 6: 6 red, 1 blue, 14 green; 2 blue, 1 red, 2 green\n",
            "Game 7: 6 red, 1 blue, 23 green; 15 blue, 1 red, 2 green\n",
            "Game 8: 6 red, 1 blue, 23 green; 2 blue, 13 red, 2 green\n"
        ]
        guesser = Guesser(data)
        result = guesser.probe()
        assert result == 8
