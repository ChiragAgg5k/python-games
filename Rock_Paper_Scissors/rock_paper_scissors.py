import random

USER_WIN = 0
COMP_WIN = 0
DRAWS = 0

options = ['rock', 'paper', 'scissor']
print("""

█▀▀█ █▀▀█ █▀▀ █░█ ░░ █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ ░░ █▀▀ █▀▀ ░▀░ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ 
█▄▄▀ █░░█ █░░ █▀▄ ▀▀ █░░█ █▄▄█ █░░█ █▀▀ █▄▄▀ ▀▀ ▀▀█ █░░ ▀█▀ ▀▀█ ▀▀█ █░░█ █▄▄▀ ▀▀█ 
▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░▀ ░░ █▀▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░▀▀ ░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀
""")
print("""Rock-Paper-scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes.
Here you will be playing against a computer which chooses its moves at random (Your odds of winning are 1/3!) \n
------REMEMBER------
Rock beats scissors, 
Paper beats rock, and 
Scissors beats paper.
---------------------\n
Lets start the game!
""")

while True:
    user_input = input(
        "\nChoose Rock/Paper/Scissor , or press Q to quit:").lower()

    if user_input == 'q':
        break
    if user_input not in options:
        print("Choose valid option....")
        continue

    pick = random.randint(0, 2)
    comp_pick = options[pick]

    print(f"The computer has picked {comp_pick}.")

    if comp_pick == 'rock' and user_input == 'paper':
        print("You won!")
        USER_WIN += 1

    elif comp_pick == 'paper' and user_input == 'scissor':
        print('You won!')
        USER_WIN += 1

    elif comp_pick == 'scissor' and user_input == 'rock':
        print('You won!')
        USER_WIN += 1

    elif comp_pick == user_input:
        print('Its a draw.')
        DRAWS += 1

    else:
        print("You lost.")
        COMP_WIN += 1

print(f"\nYour total number of wins={USER_WIN}")
print(f"Total wins of the computer={COMP_WIN}")
print(f"Total number of draws= {DRAWS}")
