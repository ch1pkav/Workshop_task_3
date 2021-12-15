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
it looks like this:"""





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
