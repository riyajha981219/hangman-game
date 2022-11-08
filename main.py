"""Hangman Game
Computer selects a word and user guesses it by giving letters a limited no. of times (no. of distinct words +2)
"""
from random import shuffle

words = ["inveigle", "aplomb", "capricious", "obsequious", "indolent"]

# shuffle the words, so you always get random words
wordsShuffled = shuffle(words)

# get the first word from the list
word = words[0]
hangman = True

# this helps keep track of how many letters are still to be guessed and
# helps representing the strings with letters that were guessed right and their positions
found = list("_"*len(word))


class Guess:
    # constructor takes word as input
    def __init__(self, word):
        self.word = word

    # calculates length of the distinct word (eleminates repetitive letters in the word (just keeps one))
    # set() function removes all the repetitive letters from the string
    def disLength(self):
        self.original = set(self.word)
        stringElement = len(self.original)
        return stringElement

    # game starts
    def game(self):
        length = self.disLength()
        count = length+2
        hangman = True
        print("_" * len(self.word))

        # loops until guesses are over and the word has not been guesses
        while count > 0 and hangman:
            print(f"\nYou have {count} guesses left!! \n")
            keyword = input("\nEnter your guess: ").lower()

            # loops until either the keyword if more than one or it is not a letter but a number
            while len(keyword) != 1 or keyword in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                keyword = input("\nEnter only one character: ").lower()

            # if found is not full
            if "_" in found:

                # if keyword is in word: traverse the list and increment inc each time you find the letter and
                # later loop through that counter and remove all the places the keyword matches
                # simultaneously print the letters on their correct position, helping the user guess the word
                if keyword in word:
                    inc = 0
                    for key in range(len(word)):
                        if keyword == word[key]:
                            inc += 1
                            found[key] = keyword

                # else ask user to try again
                else:
                    print("try again !")

                # count keeps decreasing for each try
                count -= 1

            # print the word that you guessed each time
            # first argument tells the function what to insert after each element, to add nothing put an empty string with no spaces
            # .join(<list>) gives the list to be converted
            print("\n"+"".join(found)+"\n")

            # if there was no _ in found, that means the word was guessed completely and user won!
            # put hangman=False to get out of the loop before the no. of guesses is over
            if "_" not in found:
                print("Bravo! You won!😍\n")
                hangman = False

        # if hangman is true that means the user couldn't guess the word and "HANGMAN!"
        if hangman:
            print(
                f"\nHANGMAN!!😣\n The word was {word}")


# create object and start game
guess = Guess(word)
guess.game()
