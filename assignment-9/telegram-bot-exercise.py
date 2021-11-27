from telebot import TeleBot
from telebot import types
from random import randint
from time import sleep
from khayyam import JalaliDatetime
from gtts import gTTS
from qrcode import make

bot = TeleBot('Use your token to access the HTTP API')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Greetings dear %s' % message.from_user.first_name)
    sleep(1)
    bot.send_message(
        message.chat.id, 'Command process done\nYou may try a command')


random_number = randint(-20, 20)
markup = types.ReplyKeyboardMarkup(row_width=1)
btn = types.KeyboardButton('New Game')
markup.add(btn)


@bot.message_handler(commands=['game'])
def start_game(message):
    msg = bot.send_message(
        message.chat.id, 'Wellcome to number guessing game\nGuess the number!\nTo close this command process send Exit',
        reply_markup=markup)
    bot.register_next_step_handler(msg, number_guessing_game)


def number_guessing_game(message):
    if message.text == 'Exit':
        bot.send_message(message.chat.id, 'Command Operation Ended\nYou may try a command',
                         reply_markup=types.ReplyKeyboardRemove(selective=True))
    else:
        try:
            if message.text == 'New Game':
                global random_number
                random_number = randint(-20, 20)
                bot.send_message(message.chat.id, 'Game restarted. Guess the number:',
                                 reply_markup=markup)
                bot.register_next_step_handler_by_chat_id(
                    message.chat.id, number_guessing_game)
            elif int(message.text) < random_number:
                msg = bot.send_message(
                    message.chat.id, 'Your guess is less than Goal', reply_markup=markup)
                bot.register_next_step_handler(msg, number_guessing_game)
            elif int(message.text) > random_number:
                msg = bot.send_message(
                    message.chat.id, 'Your guess is greater than Goal', reply_markup=markup)
                bot.register_next_step_handler(msg, number_guessing_game)
            else:
                bot.send_message(message.chat.id, 'Yes, That\'s right!',
                                 reply_markup=types.ReplyKeyboardRemove(selective=True))
                sleep(1)
                bot.send_message(
                    message.chat.id, 'Command process done\nYou may try a command')
        except:
            msg = bot.send_message(
                message.chat.id, 'Please send an integer number or send Exit', reply_markup=markup)
            bot.register_next_step_handler(msg, number_guessing_game)


@bot.message_handler(commands=['age'])
def send_age(message):
    msg = bot.send_message(
        message.chat.id, 'Send the date of birth in form: year/month/day\nTo close this command process send Exit')
    bot.register_next_step_handler(msg, calculating_age)


def calculating_age(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'Command Operation Ended\nYou may try a command')
    else:
        try:
            if len(message.text.split('/')) == 3:
                date_difference = JalaliDatetime.now(
                ) - JalaliDatetime(message.text.split('/')[0], message.text.split('/')[1], message.text.split('/')[2])
                bot.send_message(message.chat.id, 'You are ' +
                                 str(date_difference.days // 365) + ' years old')
                sleep(1)
                bot.send_message(
                    message.chat.id, 'Command process done\nYou may try a command')
            else:
                msg = bot.send_message(
                    message.chat.id, 'Please send expected input or send Exit')
                bot.register_next_step_handler(msg, calculating_age)
        except:
            msg = bot.send_message(
                message.chat.id, 'Please send expected input or send Exit')
            bot.register_next_step_handler(msg, calculating_age)


@bot.message_handler(commands=['voice'])
def send_voice(message):
    msg = bot.send_message(
        message.chat.id, 'Send an English sentence\nTo close this command process send Exit')
    bot.register_next_step_handler(msg, voice_process)


def voice_process(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'Command Operation Ended\nYou may try a command')
    else:
        try:
            content = gTTS(text=message.text, slow=False)
            content.save('voice.ogg')
            content = open('voice.ogg', 'rb')
            bot.send_voice(message.chat.id, content)
            sleep(1)
            bot.send_message(
                message.chat.id, 'Command process done\nYou may try a command')
        except:
            msg = bot.send_message(
                message.chat.id, 'Please send expected input or send Exit')
            bot.register_next_step_handler(msg, voice_process)


@bot.message_handler(commands=['max'])
def send_max(message):
    msg = bot.send_message(
        message.chat.id, 'Send some numbers in form: 1,2,3,4,5 to find the maximum\nTo close this command process send Exit')
    bot.register_next_step_handler(msg, find_max)


def find_max(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'Command Operation Ended\nYou may try a command')
    else:
        try:
            numbers = list(map(int, message.text.split(',')))
            bot.send_message(
                message.chat.id, 'Maximum number is: ' + str(max(numbers)))
            sleep(1)
            bot.send_message(
                message.chat.id, 'Command process done\nYou may try a command')
        except:
            msg = bot.send_message(
                message.chat.id, 'Please send expected input or send Exit')
            bot.register_next_step_handler(msg, find_max)


@bot.message_handler(commands=['argmax'])
def send_argmax(message):
    msg = bot.send_message(
        message.chat.id, 'Send some numbers in form: 1,2,3,4,5 to find the maximum index\nTo close this command process send Exit')
    bot.register_next_step_handler(msg, find_argmax)


def find_argmax(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'Command Operation Ended\nYou may try a command')
    else:
        try:
            numbers = list(map(int, message.text.split(',')))
            bot.send_message(message.chat.id, 'Maximum number index(zero based) is: ' +
                             str(numbers.index(max(numbers))))
            sleep(1)
            bot.send_message(
                message.chat.id, 'Command process done\nYou may try a command')
        except:
            msg = bot.send_message(
                message.chat.id, 'Please send expected input or send Exit')
            bot.register_next_step_handler(msg, find_argmax)


@bot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    msg = bot.send_message(
        message.chat.id, 'Send something to find its QR-Code\nTo close this command process send Exit')
    bot.register_next_step_handler(msg, find_qrcode)


def find_qrcode(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'Command Operation Ended\nYou may try a command')
    else:
        try:
            qrcode_img = make(message.text)
            qrcode_img.save('QR-Code.png')
            photo = open('QR-Code.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            sleep(1)
            bot.send_message(
                message.chat.id, 'Command process done\nYou may try a command')
        except:
            msg = bot.send_message(
                message.chat.id, 'Somethong went wrong!\nPlease send expected input or send Exit')
            bot.register_next_step_handler(msg, find_qrcode)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     '/start -> Wellcome message\n/game -> Number guessing game\n/age -> Calculates your age (Solar hijri)\n/voice -> Converts text to voice\n/max -> Finds maximum number\n/argmax -> Finds maximum number index\n/qrcode -> Makes QR-Code\n/help -> Commands guide')


bot.polling(none_stop=True)
