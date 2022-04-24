from util.game_logic import TicTacToe
from util.player import Player


def main():
    tic_tac_toe = TicTacToe()
    player_1 = Player("Player 1", "O")
    player_2 = Player("Player 2", "X")

    print("Welcome to TicTacToe!")
    print(tic_tac_toe)

    while not tic_tac_toe.end_game:
        tic_tac_toe.gameplay(player_1)
        if tic_tac_toe.draw is True or tic_tac_toe.end_game is True:
            break
        tic_tac_toe.gameplay(player_2)


if __name__ == "__main__":
    main()
