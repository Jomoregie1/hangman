'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.guessed_letters = set()
        self.unique_letters = len(self.word)
        self.isguesscorrect = False
        print(f"The mistery word has {len(self.word_guessed)} characters.")
        print(self.word_guessed)

    def check_letter(self, letter) -> None:
        """
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        """

        char_list = [char.lower() for char in self.word]
        for i in range(len(char_list)):
            if char_list[i] == letter.lower():
                self.word_guessed[i] = letter.lower()
                self.unique_letters -= 1
                self.isguesscorrect = True

        if not self.isguesscorrect:
            self.num_lives -= 1

        self.guessed_letters.add(letter.lower())
        self.isguesscorrect = False
        print(f"{self.word_guessed} | Current life: {self.num_lives}")

    def ask_letter(self):
        """
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        """

        while self.num_lives > 0 and self.unique_letters > 0:
            letter = input("Enter a letter here: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character.")
            elif letter in self.guessed_letters:
                print(f"{letter} was already tried.")
            else:
                self.check_letter(letter)

        if self.num_lives > 0 and self.unique_letters == 0:
            self.isguesscorrect = True


def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    if game.isguesscorrect:
        print("Congratulations! You Won!")
    else:
        print(f"You Lost! The word was {game.word}")


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

