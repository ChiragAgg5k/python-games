import random


class figure():
    def __init__(self) -> None:

        self.base = """
        ---------------
        |      | 
        |      
        |
        |
        |
        ^^^^^^^^^^^^^^^
        """

        self.hang1 = """
        ---------------
        |      | 
        |      O
        |
        |
        |
        ^^^^^^^^^^^^^^^
        """

        self.hang2 = """
        ---------------
        |      | 
        |      O
        |      |
        |
        |
        ^^^^^^^^^^^^^^^
        """

        self.hang3 = """
        ---------------
        |      | 
        |      O
        |      |-
        |
        |
        ^^^^^^^^^^^^^^^
        """

        self.hang4 = """
        ---------------
        |      | 
        |      O
        |     -|-
        |
        |
        ^^^^^^^^^^^^^^^
        """

        self.hang5 = """
        ---------------
        |      | 
        |      O
        |     -|-
        |     /
        |
        ^^^^^^^^^^^^^^^
        """

        self.hang6 = """
        ---------------
        |      | 
        |      O
        |     -|-
        |     / \\
        |
        ^^^^^^^^^^^^^^^
        """
        self.hanglist = [self.base, self.hang1, self.hang2,
                         self.hang3, self.hang4, self.hang5]

    def __iter__(self):
        self.currenthang = 0
        return self

    def __next__(self):

        if self.currenthang < len(self.hanglist):
            x = self.hanglist[self.currenthang]
            self.currenthang += 1
            return x

        raise StopIteration

    def __str__(self) -> str:
        return self.hanglist[self.currenthang]


class word():

    def __init__(self) -> None:
        self.word_list = ["absence", "abuse", "account", "accident", "beneath", "bend", "benefit", "biology", "bitter", "candidate", "campaign", "camera", "capacity", "capture", "deaf", "daughter", "deal", "decorate", "dialogue", "economy", "finance", "educate", "efficient",
                          "supportive", "elderly", "flight", "folk", "flame", "frustration", "garbage", "gather", "gentle", "global", "hilarious", "intelligence", "jazz", "knife", "longevity", "momument", "nonsense", "nobody", "turmeric", "utilize", "sashimi", "reconfigure", "wheat", "yellowish", "zone"]

    def random_word(self):
        return random.choice(self.word_list)

    def add_word(self, name):
        if name not in self.word_list:
            self.word_list.append(name)

    def show_words(self):
        print("\n---------------")
        for i, j in enumerate(self.word_list):
            print("{:>3}  |  {:<3}".format(i+1, j))
        print("---------------\n")


game_on = True

while game_on:
    hangman = figure()
    hangiter = iter(hangman)

    wordz = word()
    chosen = wordz.random_word()

    blank = ["_"]*len(chosen)

    print(hangman.__next__())

    while "".join(blank) != chosen:

        print("".join(blank))

        player_guess = input("Player enter your guess : ")

        if player_guess in chosen:
            index_pos = [i for i, j in enumerate(chosen) if player_guess == j]
            for i in index_pos:
                blank[i] = list(chosen)[i]

        else:
            try:
                print(hangiter.__next__())
            except StopIteration:
                print(hangman.hang6)
                print("GAME OVER")
                print("THE WORD WAS ", chosen)
                break

    cont = input("Do you want to play one more round? (y/n) : ")
    if cont != "y":
        break
