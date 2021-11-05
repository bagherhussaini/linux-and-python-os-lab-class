from time import sleep
words = []


def show_menu():
    print('┌─────────────────────────────────────────────────┐')
    print('│         1.Add New Word                          │')
    print('│         2.Translation English to Persian        │')
    print('│         3.Translation Persian to English        │')
    print('│         4.Exit                                  │')
    print('└─────────────────────────────────────────────────┘')


def load_data():
    try:
        f = open('words_bank.txt', 'r')
    except FileNotFoundError:
        print('File Not Found')
        exit()
    data = f.read()
    lines = data.split('\n')
    for i in range(0, len(lines), 2):
        words.append({'eng': lines[i], 'per': lines[i+1]})


def add_word():
    new_word = {'eng': input('Enter Your English Word: ')}
    for word in words:
        if new_word['eng'] == word['eng']:
            print('This Word Already Exists!')
            break
    else:
        new_word['per'] = input('Enter Your Persian Word: ')
        words.append(new_word)
        f = open('words_bank.txt', 'a')
        f.write('\n' + new_word['eng'] + '\n' + new_word['per'])
        f.close()
        print('Successfully Added.')


def sentence_delimiter(text: str):
    return text.split('.')


def word_delimiter(text: str):
    return text.split(' ')


def translate_english_to_persian():
    input_text = input('Enter Your English Text: ')
    user_sentences = sentence_delimiter(input_text)
    output_text = ''
    for user_sentence in user_sentences:
        user_words = word_delimiter(user_sentence)
        for user_word in user_words:
            for word in words:
                if user_word == word['eng']:
                    output_text += word['per'] + ' '
                    break
            else:
                output_text += user_word + ' '
    return output_text


def translate_persian_to_english():
    input_text = input('Enter Your Persian(Fenglish) Text: ')
    user_sentences = sentence_delimiter(input_text)
    output_text = ''
    for user_sentence in user_sentences:
        user_words = word_delimiter(user_sentence)
        for user_word in user_words:
            for word in words:
                if user_word == word['per']:
                    output_text += word['eng'] + ' '
                    break
            else:
                output_text += user_word + ' '
    return output_text


def main():
    load_data()
    while True:
        show_menu()
        choice = int(input('Choose an Option: '))
        if choice == 1:
            add_word()
            sleep(2.5)
        elif choice == 2:
            print('Translation Result: ', translate_english_to_persian())
            sleep(2.5)
        elif choice == 3:
            print('Translation Result: ', translate_persian_to_english())
            sleep(2.5)
        elif choice == 4:
            exit()
        else:
            print('Choose Correctly!')


if __name__ == '__main__':
    main()
