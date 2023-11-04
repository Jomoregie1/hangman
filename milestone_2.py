import random


word_list = ["sharon fruit", "apple", "banana", "grapes", "avocado"]
word = random.choice(word_list)
print(word)


guess = input("Enter a single letter here: ")

if len(guess) == 1 and guess.isalpha():
	print("Good guess")
else:
	print("Oops! That is not a valid input.")


