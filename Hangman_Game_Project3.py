print("Welcome to Hangman Game!")

import random

words_list=['apple','beautiful','potato','python']
choosen_word=random.choice(words_list)
lives=6
print(choosen_word)
display=[]
for i in range(len(choosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over :
    guessed_letter=input("Guess a letter : ").lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")


    if '_' not in display:
        game_over=True
        print('you win!')
