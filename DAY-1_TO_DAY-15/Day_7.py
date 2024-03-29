'''making the hangman game'''
import random

guessed_letters=[]
the_words = ['python', 'java', 'kotlin', 'javascript','laptops','tablets','phones','rap','jazz']
wrong_guess = 0
max_wrong_guesses= 5

    
word = random.choice(the_words)
print('H-A-N-G-M-A-N')
play = input("Welcome to Hangman. Do you want to play? (Y/N) ").lower()
print('pssst, the solution is ', word)
while True:
    
    if play == 'n':
        print('Thank you for visiting. Bye!')
        break
    elif play == 'y':
        user_choice = input('Enter a letter that you think is in the word: ').lower()
        if user_choice in guessed_letters:
            print("#Already guessed !!")
            continue
        guessed_letters.append(user_choice)
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word you guessed:", display_word)
    
    if len(user_choice) != 1 or not user_choice.isalpha():
        print("Please enter a single letter.")
        continue

    elif user_choice in word:
        print('Right guess')
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break
    elif user_choice not in word:
        print('Wrong guess')
        wrong_guess += 1
        print('Gesses Left: ', max_wrong_guesses - wrong_guess)
        if wrong_guess >= max_wrong_guesses:
            print('Wrong guesses: ', wrong_guess)
            print('You lose')
            print('The word is', word)
            break