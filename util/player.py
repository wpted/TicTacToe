class Player:
    def __init__(self, name, symbol):
        """
        Player symbol Limited to "X", "O"
        """
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"Player name: {self.name}\n" \
               f"Player symbol: {self.symbol}"

    @classmethod
    def input(cls):
        """
        Takes input from user.
        Returns the position (row, col)
        Inputs should follow:
        - Column and Row indexes [1, 3]
        - Inputs can't be other than Integers
        """
        valid_input = False

        while not valid_input:
            try:
                print("\nInput format(row, column)")
                row = int(input("Which row do your want to place: "))
                assert 1 <= row <= 3, "Invalid index for row, should be between 1 and 3. "

                col = int(input("Which column do your want to place: "))
                assert 1 <= col <= 3, "Invalid index for column, should be between 1 and 3."

                if 1 <= row <= 3 and 1 <= col <= 3:
                    valid_input = True

            except ValueError as e:
                print(f"-- Try Again: {e}\n")
            except AssertionError as e:
                print(f"-- Try Again: {e}\n")

        return row, col


def main():
    p1 = Player("Victoria", "X")

    print(p1)
    print(p1.input())


if __name__ == "__main__":
    main()
