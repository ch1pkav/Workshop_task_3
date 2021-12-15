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
    return """
Hello! Welcome to the Battleship game in which your
main task is to destroy all the enemys ships with right
choices to fire.
"""


def shot(showed_board: list):
    """
    takes coordinates of players shot
    """
    print("""
Now you are provided with a shot, choose right coordinates
to fire enemys ships.
""")

    for row in board:
        print(" ".join(row))

    fire_col = input("Enter your shot column coord (0-4): ")
    fire_row = input("Enter your shot row coord (0-4): ")

    player_shot_row=int(input('Guess row:'))
    player_shot_col=int(input('Guess col:'))
    while player_shot_row >4 or player_shot_col>4 or player_shot_row <0 or player_shot_col<0:
        print('This point is not in the sea')
        player_shot_row=int(input('Guess row:'))
        player_shot_col=int(input('Guess col:'))
        if player_shot_row <=4 and player_shot_col<=4 and player_shot_row >=0 and player_shot_col>=0:
            break
    if showed_board[player_shot_row][player_shot_col]=='B':
        print('Congrats! You guessed')
        showed_board[player_shot_row][player_shot_col] = 'X'
    else:
        print('You missed')
    return showed_board

if __name__ == "__main__":
    main()
