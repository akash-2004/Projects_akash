import random
from hangman_art import logo, stages
from hangman_words import word_list

random_word = word_list[random.randint(0, 2)]
mysterio = list("_"*len(random_word))
lives = 6
current = []
for c in random_word:
    current += c

print(f'''
{logo}

Welcome to Hangman ☠

Psst 🤫, the word is {random_word}😉
''')

while lives != 0:
    letter = input("Guess a letter: ").lower()
    yayORnay = 0
    if letter in mysterio:
        print(f"You've already guessed {letter}")
    elif len(letter.strip()) != 1:
        print("Guess a valid letter")
    else:
        for i in range(len(random_word)):
            if current[i] == letter:
                mysterio[i] = letter
                yayORnay += 1

        if yayORnay == 0:
            lives -= 1
            print(f'You have {lives} chances left')
    print(f'{" ".join(mysterio)}')
    print(stages[lives])

    if current == mysterio:
        break


final_word = ''.join(mysterio)

if final_word == random_word:
    print(final_word)
    print("Congrats! You guessed the right word")
else:
    print(f"The correct word was {random_word}. Better luck next time")
