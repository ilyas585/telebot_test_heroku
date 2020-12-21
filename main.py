import telebot

bot = telebot.TeleBot("1471937524:AAHZ7ZkwN6TGSiTPv__fCcDBgiVmNJYzShk")

@bot.message_handler(commands=["wakeup"])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row("programming(price)", "english(price)")
    bot.send_message(message.chat.id, "choose course", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "programming(price)":
        bot.send_message(message.chat.id, 'Cost: 6500r per month for 9 lessons of 2 hours')
    elif message.text.lower() == "english(price)":
        bot.send_message(message.chat.id, "Cost: 900 ruble 1 hour 2 time in week")


bot.polling()
