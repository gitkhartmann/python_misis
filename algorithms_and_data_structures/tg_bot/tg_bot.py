import telebot
from telebot import types

token = ''

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет!\nМогу подкинуть тебе пару интересных ссылок, введи команду /button')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('My GitHub')
    item2 = types.KeyboardButton('YouTube')
    item3 = types.KeyboardButton('Google')
    item4 = types.KeyboardButton('Yandex')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Выбирай что желаешь', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message.text)

    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Салам бродяга')
    elif message.text == 'My GitHub':
        bot.send_message(message.chat.id, 'https://github.com/gitkhartmann')
    elif message.text == 'YouTube':
        bot.send_message(message.chat.id, 'https://youtube.com')
    elif message.text == 'Google':
        bot.send_message(message.chat.id, 'https://google.com')
    elif message.text == 'Yandex':
        bot.send_message(message.chat.id, 'https://dzen.ru/')


if __name__ == '__main__':
    bot.infinity_polling()
