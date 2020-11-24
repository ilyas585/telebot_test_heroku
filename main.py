import telebot

bot = telebot.TeleBot("1471937524:AAHZ7ZkwN6TGSiTPv__fCcDBgiVmNJYzShk")

@bot.message_handler(commands=["wakeup"])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row("Прогроммирование(стоимость)", "Английский(стоимость)")
    bot.send_message(message.chat.id, "Выберите курс", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "прогроммирование(стоимость)":
        bot.send_message(message.chat.id, 'Стоимость: 6500р в месяц за 9 занятий по 2 часа')
    elif message.text.lower() == "английский(стоимость)":
        bot.send_message(message.chat.id, "900р за 1 урок в 2 часа")


bot.polling()