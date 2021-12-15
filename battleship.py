

def board():
    """
    creates game board
    """

    field = []
    for x in range(5):
        field.append(["O"] * 5)

    for row in field:
        print(" ".join(row))

    return field


def shot():
    """
    takes coordinates of player's shot
    """

    fire_col = input("Enter your shot column coord (0-4): ")
    fire_row = input("Enter your shot row coord (0-4): ")


board()
