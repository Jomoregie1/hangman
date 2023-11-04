import random


class Hangman:
    """
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
    """

    def __init__(self, word_list: list[str], num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]

        # I used a set here instead of a list because it quicker to make comparisons O(1) compared with O(n) for a list.
        self.list_of_guesses = set()
        self.num_letters = len(self.word)

        print(f"The mistery word has {len(self.word_guessed)} characters.")
        print(self.word_guessed)

    def check_letter(self, letter: str) -> None:
        """
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        """

        isGuessCorrect = False

        char_list = [char.lower() for char in self.word]
        for i in range(len(char_list)):
            if char_list[i] == letter:
                self.word_guessed[i] = letter
                self.num_letters -= 1
                isGuessCorrect = True

        if not isGuessCorrect:
            self.num_lives -= 1

        self.list_of_guesses.add(letter)
        print(f"{self.word_guessed} | Current life: {self.num_lives}")

    def ask_letter(self) -> bool:
        """
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        """

        while self.num_lives > 0 and self.num_letters > 0:
            letter = input("Enter a letter here: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.list_of_guesses:
                print(f"{letter} was already tried.")
            else:
                self.check_letter(letter)

        return self.num_letters == 0


def play_game(word_list: list[str]) -> None:
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    isGameWon = game.ask_letter()
    if isGameWon:
        print("Congratulations! You Won!")
    else:
        print(f"You Lost! The word was {game.word}")


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
