import random


fav_fruits = ['apple','banana','avocado','watermelon','dates']
computers_choice = random.choice(fav_fruits)
set_of_letters = {char for char in computers_choice}



def check_guess(guess):
	guess.lower()
	if len(guess) == 1 and guess.isalpha():
		if guess in set_of_letters:
			print(f"Good guess!{guess}")
			return True
		else:
			print(f"Sorry, {guess} is not in the word. Try again.")
	else:
		print("Invalid letter.Please, enter a single alphabetical character.")
	
	return False



def ask_for_input():
	while True:
		guess = input("Enter a letter here: ")
		if len(guess) == 1 and guess.isalpha():
			break
	return guess





while True:
	guess = ask_for_input()
	check = check_guess(guess)
	if check == True:
		break
		
