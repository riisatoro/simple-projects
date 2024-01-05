"""
Simple rock paper scissors game.
"""
import random
import sys

import emoji


class RockPaperScissors:
    def __init__(self):
        print("Welcome to Rock Paper Scissors!")
        self.moves_emoji: dict = {
            "rock": emoji.emojize(":rock:"),
            "paper": emoji.emojize(":page_facing_up:"),
            "scissors": emoji.emojize(":scissors:"),
        }
        self.valid_moves: list = ["rock", "paper", "scissors"]
        self.win_combination: dict = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

    def get_player_move(self):
        player_move = input("Rock, paper or scissors? >> ").lower()
        if player_move in ["quit", "exit"]:
            print("Thanks for playing!")
            sys.exit()

        if player_move not in self.valid_moves:
            print("Invalid move. Try again.")
            return self.get_player_move()
        return player_move

    def get_ai_move(self):
        return random.choice(self.valid_moves)

    def display_move(self, player_move: str, ai_move: str):
        print("- - - - - - -")
        print(f"You: {self.moves_emoji[player_move]}")
        print(f"AI: {self.moves_emoji[ai_move]}")
        print("- - - - - - -")

    def define_winner(self, player_move: str, ai_move: str):
        if player_move == ai_move:
            print("It's a tie!")
            return

        if ai_move == self.win_combination[player_move]:
            print("You win!")
        else:
            print("You lose!")
        sys.exit()

    def run(self):
        player_move = self.get_player_move()
        ai_move = self.get_ai_move()
        self.display_move(player_move, ai_move)
        self.define_winner(player_move, ai_move)
        self.run()


if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
