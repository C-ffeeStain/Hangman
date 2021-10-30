"""Hangman, but a simple version in the CLI."""

import json
import random
import os
import sys
from platform import system
from time import sleep

# get the words from the json file
with open("data/words.json") as f:
    words: dict = json.load(f)


def main(first_time: bool = True) -> None:
    # the list of guessed letters
    guessed_letters = []

    # max number of guesses is 10
    max_guesses = 10

    # choose a random category
    category = random.choice(list(words.keys()))

    # choose a random word from that category
    word = random.choice(words[category])

    # create a list of the letters in the word
    letters = list(word)

    # create a list of the letters in the word, with dashes
    hidden_letters = []
    for letter in letters:
        hidden_letters.append("_") if letter != " " else hidden_letters.append(" ")

    if first_time:
        print("Welcome to Hangman!")
        print("Type 'guess' and then a letter to guess a letter.")
        print("Type 'quit' to exit the game.")
        print("Type 'help' to see the rules.")
        print("Type 'new' to start a new game.")
        print("Type 'load' to load a saved game.")
        print("Type 'save' to save the current game.")
        print("Type 'about' to see the about section.")
        print("Type 'credits' to see the credits section.")
        print("Type 'version' to see the version of the game.\n")
        # count down to 5 seconds and use \r to overwrite the previous line
        for i in range(5, 0, -1):
            print(f"Starting in {i} seconds...", end="\r")
            sleep(1)

    while True:
        if system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        # if the user runs out of guesses, the game ends
        if max_guesses == 0:
            print("You ran out of guesses. The word was: " + word)
            if input("Would you like to play again (y/n)? ").lower() in (
                "yes",
                "y",
                "true",
                "t",
            ):
                main(False)
            else:
                sys.exit()
        # if the user has guessed all the letters, the game ends
        if "_" not in hidden_letters:
            print("You guessed all the letters! The word was: " + word)
            if input("Would you like to play again (y/n)? ").lower() in (
                "yes",
                "y",
                "true",
                "t",
            ):
                main(False)
            else:
                sys.exit()

        # print the category, the hidden letters, and the number of guesses left
        print(f"Category: {category}")
        print(" ".join(hidden_letters))
        print("Guessed letters: " + ", ".join(guessed_letters))
        print(f"You have {max_guesses} guesses left.")

        # get the next command
        cmd = input(">> ")

        # check if the user wants to quit
        if cmd == "quit":
            sys.exit()
        elif cmd.startswith("guess"):
            # get the letter
            letter = cmd.split(" ")[1]
            if letter in guessed_letters:
                print(f"You already guessed '{letter}'!\n")
                sleep(0.75)
                continue
            elif len(letter) != 1:
                print("You can only guess one letter at a time!\n")
                sleep(0.75)
                continue
            elif letter not in letters:
                print(f"That letter is not in the word!\n")
                max_guesses -= 1
                guessed_letters.append(letter)
                sleep(0.75)
                continue
            else:
                # replace the dashes with the letter
                for i, l in enumerate(letters):
                    if l == letter:
                        hidden_letters[i] = letter
                guessed_letters.append(letter)
                sleep(0.5)
        elif cmd == "help":
            print(
                "This is a simple version of the classic game 'Hangman.' \n"
                + "The goal is to guess the word before the number of guesses"
                + " runs out."
            )
            sleep(2)
            continue
        else:
            print("Invalid command!\n")
            sleep(0.75)
            continue


if __name__ == "__main__":
    main()
