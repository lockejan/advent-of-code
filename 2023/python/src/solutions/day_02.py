from src.utils.solution_base import SolutionBase


class Solution(SolutionBase):
    blue_max = 14
    green_max = 13
    red_max = 12

    def _is_possible_game(self, game: dict[int, dict[str, int]]) -> bool:
        game_id = list(game.keys())[0]
        samples = game.get(game_id, dict())
        if samples.get("blue", 0) > self.blue_max:
            return False
        if samples.get("green", 0) > self.green_max:
            return False
        if samples.get("red", 0) > self.red_max:
            return False
        return True

    def _count_should_update(self, color, count, round) -> bool:
        if color == "blue":
            return count > round.get("blue", 0)
        elif color == "green":
            return count > round.get("green", 0)
        elif color == "red":
            return count > round.get("red", 0)
        return False

    def _parse_stats(self, game_stats) -> dict[str, int]:
        game_parts = game_stats.replace(";", ",").split(",")
        game_parts = [part.strip().split(' ') for part in game_parts]
        game_seq = list()
        for sample in game_parts:
            game_seq.extend(reversed(sample))
        color, count = game_seq[0::2], list(map(int, game_seq[1::2]))
        rounds = dict()
        for color, count in zip(color, count):
            if self._count_should_update(color, count, rounds):
                rounds[color] = count
        return rounds

    def _parse(self, game: str) -> dict[int, dict[str, int]]:
        game = game.replace("Game ", "")
        game_id, game_stats = game.split(":")
        rounds = self._parse_stats(game_stats)

        return {game_id: rounds}

    def part1(self) -> int:
        parsed_data = [self._parse(game) for game in self.data]
        games = [
            list(game.keys())[0] for game in parsed_data
            if self._is_possible_game(game)
        ]
        return sum(map(int, games))

    def part2(self) -> int:
        parsed_data = [self._parse(game) for game in self.data]
        power = lambda x: x.get("blue", 0) * x.get("green", 0) * x.get(
            "red", 0)
        power_of_games = [
            power(game.get(list(game.keys())[0], dict()))
            for game in parsed_data
        ]
        return sum(power_of_games)
