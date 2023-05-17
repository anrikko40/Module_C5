import telebot
from config import keys, TOKEN
from extensions import ConvertionExcepcion, CriptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду в следующем формате:\n<имя вылюты> \
<В какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExcepcion('Неверный запрос. Используйте комманду /help')


        quote, base, amount = values
        total_base = CriptoConverter.convert(quote, base, amount)
    except ConvertionExcepcion as e:
        bot.reply_to(message, f'Ошибка пользователья\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Неудалось отправить команду\n{e}')
    else:
         text = f'Цена {amount} {quote} в {base} - {total_base}'
         bot.send_message(message.chat.id, text)

bot.polling()

