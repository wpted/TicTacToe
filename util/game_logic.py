import os


class TicTacToe:
    def __init__(self, end_game=False):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.end_game = end_game
        self.draw = False
        self.round = 1

    def __repr__(self):
        return f"\n{self.__class__.__name__}:\n" \
               f"     1   2   3 \n" \
               f"1    {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n" \
               f"   ----|---|----\n" \
               f"2    {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n" \
               f"   ----|---|----\n" \
               f"3    {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}\n"

    def gameplay(self, player):
        """
        Replace the board with player input.
        """

        print(f"< {player.name}: '{player.symbol}' >")
        node_empty = True
        while node_empty:
            player_input = player.input()  # (row, col)
            if self.board[player_input[0] - 1][player_input[1] - 1] == " ":
                self.board[player_input[0] - 1][player_input[1] - 1] = player.symbol
                node_empty = False
            else:
                print(f"Node{player_input} occupied, try again.\n")
        os.system('clear')  # To clear unnecessary previous prints

        self.round += 1
        print(f"{player_input=}")
        print(self)
        self.check_end_game()
        if self.end_game:
            print(f"{player.name} wins!")

    def check_end_game(self):
        """
        End the game when meet the following status
        - When row connects
        - When column connects
        - When diagonal connects
        - Draw
        """

        # Check Diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " \
                or self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            self.end_game = True

        # Check Row
        for row in self.board:
            if len(set(row)) == 1 and " " not in row:
                self.end_game = True

        # Check Column
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.end_game = True

        # Check Draw
        if self.round == 10 and self.end_game is False:  # TicTacToe can't have over 9 rounds
            self.draw = True
            print("It's a draw!")
