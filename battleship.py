"""
the battleship game
"""


def main():
    """
    the main function
    """

    greetings()

    board = board_generator()


def put_ships():
    """
    player puts their ships
    """

    print("""
Now you are to put your ships on the field.
you are provided with 4 ships:
The first ship size is: 1*3
it looks like this:
+
+
+
The second ship size is 2*1:
++

The third ship size is: 1*1
it looks like this:
+
The fourth ship size is: 1*1
it looks like this:





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


def greetings():
    """
    greetings and rules
    """

    return """
Hello! Welcome to the Battleship game in which your
main task is to destroy all the enemy's ships with right
choices to fire.
"""


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
