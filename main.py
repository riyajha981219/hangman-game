"""Hangman Game
Computer selects a word and user guesses it by giving letters a limited no. of times (6 because 6 lines make a stick-man)
"""
from random import shuffle

words = ["inveigle", "aplomb", "capricious", "obsequious", "indolent"]
wordsShuffled = shuffle(words)
word = words[0]
hangman = True
wordCopy = list(word)
found = list("_"*len(word))


class Guess:

    def __init__(self, word):
        self.word = word

    def disLength(self):
        self.original = set(self.word)
        stringElement = len(self.original)
        return stringElement

    def game(self):
        length = self.disLength()
        count = length+2
        hangman = True
        print("_" * len(self.word))

        while count > 0 and hangman:
            print(f"\nYou have {count} guesses left!! \n")
            keyword = input("\nEnter your guess: ").lower()

            while len(keyword) != 1 or keyword in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                keyword = input("\nEnter only one character: ").lower()

            if (len(wordCopy) > 0):
                if keyword in wordCopy:
                    inc = 0
                    for key in range(len(word)):
                        if keyword == word[key]:
                            inc += 1
                            found[key] = keyword

                    for i in range(inc):
                        wordCopy.remove(keyword)

                else:
                    print("try again !")
                count -= 1
            print("\n"+"".join(found)+"\n")
            if len(wordCopy) == 0:
                print("Bravo! You won!\n")
                hangman = False

        if hangman:
            print(
                f"\nHANGMAN!!\n The word was {word}")


guess = Guess(word)
guess.game()
