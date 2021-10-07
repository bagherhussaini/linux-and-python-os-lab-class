from random import randint
user_score = 0
computer1_score = 0
computer2_score = 0
loop_number = int(input('How Many Times You Want to Play: '))
for i in range(loop_number):
    print('Round ', i+1, ': ')
    user_choice = int(input('You Turn to Choice (Hand State):\n1. Foreside\n2. Backside\n'))
    while user_choice < 1 or user_choice > 2:
        user_choice = int(input('Invalid Choice!\nEnter Your Choice Correctly (Hand State):'
                                '\n1. Foreside\n2. Backside\n'))
    if user_choice == 1:
        user_choice_name = 'Foreside'
    else:
        user_choice_name = 'Backside'
    print('Now Computer 1 Turns to Choice...')
    computer1_choice = randint(1, 2)
    if computer1_choice == 1:
        computer1_choice_name = 'Foreside'
    else:
        computer1_choice_name = 'Backside'
    print('Computer 1 Hand State: ', computer1_choice_name)
    print('Now Computer 2 Turns to Choice...')
    computer2_choice = randint(1, 2)
    if computer2_choice == 1:
        computer2_choice_name = 'Foreside'
    else:
        computer2_choice_name = 'Backside'
    print('Computer 2 Hand State: ', computer2_choice_name)

    if user_choice == computer1_choice == computer2_choice:
        print('Tie! Latest Scores Below:')
    elif user_choice == 1:
        if computer1_choice == 1:
            print('Computer 2 Wins!')
            computer2_score += 1
        elif computer2_choice == 1:
            print('Computer 1 Wins!')
            computer1_score += 1
        elif computer1_choice == 2 and computer2_choice == 2:
            print('You Win!')
            user_score += 1
    elif user_choice == 2:
        if computer1_choice == 2:
            print('Computer 2 Wins!')
            computer2_score += 1
        else:
            if computer2_choice == 2:
                print('Computer 1 Wins!')
                computer1_score += 1
            else:
                print('You Win!')
                user_score += 1
    print('Your Score: ', user_score, '\tComputer 1 Score: ', computer1_score, '\tComputer 2 Score: ', computer2_score)

if user_score == computer1_score == computer2_score:
    print('Tie!')
elif (user_score > computer1_score) and (user_score > computer2_score):
    largest = user_score
    print('You Are the Final Winner!')
elif (computer1_score > user_score) and (computer1_score > computer2_score):
    largest = computer1_score
    print('Computer 1 is the Final Winner!')
elif (computer2_score > user_score) and (computer2_score > computer1_score):
    largest = computer2_score
    print('Computer 2 is the Final Winner!')
else:
    print('There Are Two Player Tied Above!')
