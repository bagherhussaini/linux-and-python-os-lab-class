from random import randint
user_score = 0
computer_score = 0
for i in range(5):
    print('Round ', i+1, ': ')
    user_choice = int(input('You Turn to Choice:\n1. Rock\n2. Paper\n3. Scissor\n'))
    while user_choice < 1 or user_choice > 3:
        user_choice = int(input('Invalid Choice!\nEnter Your Choice Correctly:\n1. Rock\n2. Paper\n3. Scissor\n'))
    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    else:
        user_choice_name = 'Scissor'
    print('Now Computer Turns to Choice...')
    computer_choice = randint(1, 3)
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissor'
    print('User Choice: ', user_choice_name, '\tVS\tComputer Choice: ', computer_choice_name)

    if user_choice == computer_choice:
        print('Tie! Latest Scores Below:')
    elif user_choice == 1:
        if computer_choice == 2:
            print('Computer Wins!')
            computer_score += 1
        else:
            print('You Win!')
            user_score += 1
    elif user_choice == 2:
        if computer_choice == 3:
            print('Computer Wins!')
            computer_score += 1
        else:
            print('You Win!')
            user_score += 1
    elif user_choice == 3:
        if computer_choice == 1:
            print('Computer Wins!')
            computer_score += 1
        else:
            print('You Win!')
            user_score += 1
    else:
        print('Something Went Wrong!')
    print('Your Score: ', user_score, '\tComputer Score: ', computer_score)
print('As You Saw, Final Scores Are:\nYour Score ---> ', user_score, '\nComputer Score ---> ', computer_score)
if user_score > computer_score:
    print('You Are the Final Winner!')
elif user_score < computer_score:
    print('Computer is the Final Winner!')
else:
    print('Tie!')