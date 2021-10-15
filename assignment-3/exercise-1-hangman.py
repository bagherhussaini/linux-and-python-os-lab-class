from random import choice
words_list = ['family', 'nature', 'study', 'programming', 'parkour',
              'relationship', 'linux', 'windows', 'python', 'cplusplus']
secret_word = choice(words_list)
game_mode = int(input('Select the Game Mode by Number:\n1.Easy\n2.Normal\n3.Hard\n'))
while game_mode <= 0 or game_mode > 3:
    game_mode = int(input('Enter 1 or 2 or 3 :|\nSelect the Game Mode by Number:\n1.Easy\n2.Normal\n3.Hard\n'))
if game_mode == 1:
    chance = 15
    print('You\'ve Selected Easy\nYou Can Try for 15 Times!(Wrong Guesses)')
elif game_mode == 2:
    chance = 10
    print('You\'ve Selected Normal\nYou Can Try for 10 Times!(Wrong Guesses)')
else:
    chance = 5
    print('You\'ve Selected Hard\nYou Can Try for 5 Times!(Wrong Guesses)')
user_true_chars = []
while chance > 0:
    already_guessed = False
    user_char_range = True
    won = True
    for chars in secret_word:
        if chars in user_true_chars:
            print(chars, end=' ')
        else:
            print('_', end=' ')
            won = False
    if won:
        print('\nCongrats! You Win.')
        break
    user_char = input('Enter a Character: ')
    user_char = user_char.lower()
    if len(user_char) != 1:
        print('Enter a Single Letter.')
    elif user_char in user_true_chars:
        already_guessed = True
        print('You\'ve already Entered this Character!')
    elif user_char not in 'abcdefghijklmnopqrstuvwxyz':
        user_char_range = False
        print('Enter a Letter!!!')
    if not already_guessed and len(user_char) == 1 and user_char_range:
        if user_char in secret_word:
            user_true_chars.append(user_char)
            print('Correct!')
        else:
            chance -= 1
            print('Incorrect')
            if chance > 0:
                print("You have", + chance, 'Chance(s)')
            if chance == 0:
                print('Game Over!')
