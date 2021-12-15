"""
the battleship game
"""


def main():
    """
    the main function
    """

    greetings()

    board = board_generator()


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


def put_ships(board: list):
    """
    player puts their ships
    """

    print("""
Now you are to put your ships on the field.
You are provided with 4 ships:

The first ship size is 1*3:
B
B
B

The second ship size is 2*1:
B
B

The third ship size is 1*1:
B

The fourth ship size is 1*1:
B
""")

    board = first_ship(board)
    board = second_ship(board)
    board = small_ship(board)
    board = small_ship(board)

    return board


def first_ship(board: list):
    """
    first ship 1*3
    """

    row = int(input("Choose left row coord for your first ship (0-4): "))
    col = int(input("Choose top column coord for your first ship (0-4): "))
    l_ship = 3
    values = [0, 1, 2, 3, 4]
    if row not in values or col not in values or l_ship + row > 4:
        print('Wrong coordinates, try again')
        return first_ship(board)

    for i in range(5):
        for j in range(5):
            if j == row and i == col and l_ship > 0:
                board[row][col] = 'B'
                row += 1
                l_ship -= 1

    return board


def second_ship(board: list):
    """
    second ship 1*2
    """

    row = int(input("Choose left row coord for your second ship (0-4): "))
    col = int(input("Choose top column coord for your second ship (0-4): "))
    l_ship = 2
    values = [0, 1, 2, 3, 4]
    if row not in values or col not in values or l_ship + row > 4:
        print('Wrong coordinates, try again')
        return second_ship(board)

    for i in range(5):
        for j in range(5):
            if j == row and i == col and l_ship > 0:
                board[row][col] = 'B'
                row += 1
                l_ship -= 1

    return board


def small_ship(board: list):
    """
    third and fourth ship
    """

    row = int(input("Choose left row coord for your small ship (0-4): "))
    col = int(input("Choose top column coord for your small ship (0-4): "))
    values = [0, 1, 2, 3, 4]
    if row not in values or col not in values or board[row][col] == 'B':
        print('Wrong coordinates, try again')
        return small_ship(board)

    for i in range(5):
        for j in range(5):
            if j == row and i == col:
                board[row][col] = 'B'

    return board


def ship_putter(board: list):


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
