#!/usr/bin/env python

from input_handler import InputHandler


class Guesser(InputHandler):
    blue_max = 14
    green_max = 13
    red_max = 12

    def is_possible_game(self, game: dict[int, dict[str, int]]) -> bool:
        game_id = list(game.keys())[0]
        samples = game.get(game_id, dict())
        if samples.get("blue", 0) > self.blue_max:
            return False
        if samples.get("green", 0) > self.green_max:
            return False
        if samples.get("red", 0) > self.red_max:
            return False
        return True

    def count_should_update(self, color, count, round) -> bool:
        if color == "blue":
            return count > round.get("blue", 0)
        elif color == "green":
            return count > round.get("green", 0)
        elif color == "red":
            return count > round.get("red", 0)
        return False

    def parse_game(self, game: str) -> dict[int, dict[str, int]]:
        game = game.replace("Game ", "")
        game_id, game_stats = game.split(":")
        game_id = int(game_id)
        game_parts = game_stats.replace(";", ",").split(",")
        game_parts = [part.strip().split(' ') for part in game_parts]

        game_seq = list()
        for sample in game_parts:
            game_seq.extend(reversed(sample))

        color, count = game_seq[0::2], list(map(int, game_seq[1::2]))
        rounds = dict()
        for color, count in zip(color, count):
            if self.count_should_update(color, count, rounds):
                rounds[color] = count

        return {game_id: rounds}

    def probe(self):
        parsed_data = [self.parse_game(game) for game in self.data]
        games = [
            list(game.keys())[0] for game in parsed_data
            if self.is_possible_game(game)
        ]
        return sum(map(int, games))


if __name__ == '__main__':
    guesser = Guesser.with_file_input("../resources/input-2.txt")
    print(f"day_02-a: {guesser.probe()}")
