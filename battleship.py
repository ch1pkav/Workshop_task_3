"""
the battleship game
"""


def main():
    """
    the main function
    """
    print(greetings())

    player1_board = board_generator()
    player2_board = board_generator()

    player1_board = put_ships(player1_board)
    player2_board = put_ships(player2_board)

    player1_won = False
    player2_won = False

    while not player1_won and not player2_won:
        print("Player 1, take a shot!")
        player2_board = shot(player2_board)
        print("Player 2, take a shot!")
        player1_board = shot(player1_board)
        player1_won = all("B" not in row for row in player2_board)
        player2_won = all("B" not in row for row in player1_board)

    if player1_won and player2_won:
        print('It\'s a tie!')
    elif player1_won:
        print("Player 1 won!")
    else:
        print("Player 2 won!")


def greetings():
    """
    greetings and rules
    """

    return """
Hello! Welcome to the Battleship game in which your
main task is to destroy all the enemy's ships with right
choices to fire.
"""


def board_generator():
    """
    generates game board
    """

    field = []
    for x in range(5):
        field.append(["O"] * 5)

    # for row in field:
    #     print(" ".join(row))

    return field


def put_ships():
    """
    player puts their ships
    """

    print("""
Now you are to put your ships on the field.
You are provided with 4 ships:

The first ship size is 1*3:
+
+
+

The second ship size is 2*1:
++

The third ship size is 1*1:
+

The fourth ship size is 1*1:
+
""")

    coord_col = input("Choose column coord for your first ship (0-4): ")
    row_col = input("Choose row coord for your first ship (0-4): ")


def shot(board: list):
    """
    takes coordinates of player's shot
    """

    print("""
Now you are provided with a shot, choose right coordinates
to fire enemy's ships.
""")

    for row in board:
        print(" ".join(row))

    fire_col = input("Enter your shot column coord (0-4): ")
    fire_row = input("Enter your shot row coord (0-4): ")


if __name__ == "__main__":
    main()
