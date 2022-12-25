import random


def show_board() -> None:
    """Prints the board in a readable format."""

    print("\n" * 100)
    print(
        """
████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝"""
    )  # repeated heading
    print()
    print("-----------")
    for i in board:
        print("   |   |")
        print(" " + i[0] + " | " + i[1] + " | " + i[2])
        print("   |   |")
        print("-----------")


def user_mark(marker: str, position: int) -> bool:
    """Sets the user's marker at the position he/she chooses.

    Args:
        marker (str): "X" or "O"
        position (int): 1-9 (position on the board)

    Returns:
        bool: True if the position is valid, False if the position is invalid.
    """

    if position % 3 == 0:
        pos1 = 2
        position = position // 3 - 1
    else:
        pos1 = position % 3 - 1
        position = position // 3

    # checking if user's chosen position is valid or not
    if board[position][pos1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        board[position][pos1] = marker
        return True

    print("\nChoose a valid option.")
    return False


def comp_mark(COMP_MARKER: str) -> None:
    """
    generates a random position for the computer to place its marker at
    if the position is preoccupied , it loops till it finds an empty position
    Important : board needs to be checked if its full or not before passing this function,
    else it will result in a infinite loop!
    """
    while True:
        # setting a random position as computer's marker's position
        comp_pos1 = random.randint(1, 9)
        comp_position = comp_pos1

        if comp_pos1 % 3 == 0:
            comp_pos2 = 2  # positions divisble by 3 will by default be at 3rd position in the row,
            # eg for position=3 , 3//3=1 => 0th index => 1st row (thats where 3rd position is.)
            comp_pos1 = comp_pos1 // 3 - 1
        else:
            # positions not divisble by 3 will have their position at remainder of division by 3.
            comp_pos2 = comp_pos1 % 3 - 1
            # no need for -1 here for index. eg 4//3=1 , which the row's index where 4 is stored.
            comp_pos1 = comp_pos1 // 3

        if board[comp_pos1][comp_pos2] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            board[comp_pos1][comp_pos2] = COMP_MARKER
            break

    show_board()
    print(f"\nThe computer played position: {comp_position}")


def win_check(board: list[list[int]], mark: str) -> bool:
    """Checks if the given mark has won the game or not.

    Args:
        board (list[list[int]]): Nested list containing the board.
        mark (str): Marker to check for.

    Returns:
        bool: True if the given mark has won the game, False otherwise.
    """
    return (
        (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark)
        or  # across the top
        # across the middle
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark)
        or
        # across the bottom
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark)
        or
        # down the middle
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark)
        or
        # down the left side
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark)
        or
        # down the right side
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark)
        or
        # diagonal
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark)
        or (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark)
    )  # diagonal


def check_filled_board():
    """
    Function to check if the board is full or not.
    If the board is full after user's or computer's marker is placed , and neither have won,
    The game has resulted in a tie.
    Meaning the board needs to be checked twice!

    """
    unique_board = []
    for i in board:
        for j in i:
            if j not in unique_board:
                unique_board.append(j)

    if unique_board in (["X", "O"], ["O", "X"]):
        return True
    return False


# main code starts


board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
USER_WINS = 0
COMP_WINS = 0

print(
    """
████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝

Tic-tac-toe is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. 
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. 
Here you will be playing against a computer which chooses its moves at random (It is very easy to win!)
Let's start the game!
"""
)  # welcome statement

while True:  # loop to get marker of user's choice
    temp_marker = input("\nEnter the marker of your choice , O or X:").upper()
    if temp_marker in ["X", "O"]:
        user_marker = temp_marker
        break
    print("Choose a valid marker.")

COMP_MARKER = ""

if user_marker == "X":  # setting computer's marker opposite to user's
    COMP_MARKER = "O"
else:
    COMP_MARKER = "X"

END_GAME = False

while END_GAME is False:  # main loop (loop for each game)

    print("\nNow we will do a coin flip to decide who goes first.")
    coin_flip = input("Choose Heads/Tails :").lower()

    if coin_flip in ["heads", "tails"]:

        random_flip = ["heads", "tails"][random.randint(0, 1)]

        if coin_flip == random_flip:
            show_board()
            print("\nThe coin landed on " + random_flip)
            print("The Player will go first!")

        else:
            comp_mark(COMP_MARKER)
            show_board()
            print("\nThe coin landed on " + random_flip)
            print("Computer has gone first!")
    else:
        print("Choose a valid option.")
        continue  # loops the main loop if coin_flip is neither heads or tails

    while True:  # sub loop (loop for each move)
        try:
            user_input = int(
                input(
                    "\nEnter the position where you want to place your marker [1-9]\nOR enter 10 to end the game:"
                )
            )
            if user_input in range(1, 10):  # [1,2,3,4,5,6,7,8,9]
                if user_mark(user_marker, user_input):
                    pass
                else:
                    continue  # loops sub loop again if user input is wrong

                if win_check(board, user_marker):

                    show_board()
                    print()
                    print("YOU WON!")
                    USER_WINS += 1
                    cont = input(
                        "\nPress y to contiue playing, \nOr press any other key to quit:"
                    )

                    if cont != "y":
                        END_GAME = True
                        break

                    board = [
                        ["1", "2", "3"],
                        ["4", "5", "6"],
                        ["7", "8", "9"],
                    ]  # setting up a new board
                    print()
                    show_board()
                    continue

                if check_filled_board():
                    print("It's a tie.")
                    cont = input(
                        "\nPress y to contiue playing, \nOr press any other key to quit:"
                    )

                    if cont != "y":
                        END_GAME = True
                        break

                    board = [
                        ["1", "2", "3"],
                        ["4", "5", "6"],
                        ["7", "8", "9"],
                    ]  # setting up a new board
                    print()
                    show_board()
                    continue

                comp_mark(COMP_MARKER)

                if win_check(board, COMP_MARKER):

                    print("Computer won...\nYou lost.")
                    COMP_WINS += 1
                    cont = input(
                        "Try again?(press y) \nOr press any other key to quit:"
                    )

                    if cont != "y":
                        END_GAME = True
                        break

                    board = [
                        ["1", "2", "3"],
                        ["4", "5", "6"],
                        ["7", "8", "9"],
                    ]  # setting up a new board
                    print()
                    show_board()
                    continue

                if check_filled_board():
                    print("It's a tie.")
                    cont = input(
                        "\nPress y to contiue playing, \nOr press any other key to quit:"
                    )

                    if cont != "y":
                        END_GAME = True
                        break

                    board = [
                        ["1", "2", "3"],
                        ["4", "5", "6"],
                        ["7", "8", "9"],
                    ]  # setting up a new board
                    print()
                    show_board()
                    continue

            elif user_input == 10:  # if user wants to end the game midway
                END_GAME = True
                break

            else:
                print("Enter a valid choice.")

        except Exception as error:
            print(f"Following error occured:{error}")


print(f"\nComputer won {COMP_WINS} times.")
print(f"You won {USER_WINS} times.\n")
