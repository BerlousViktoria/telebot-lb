import telebot

TOKEN = "8995028992:AAHiozswX9rzPlI86BqSYcxO345wqlQmYS0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")

if __name__ == '__main__':
    print("Бот запущений...")
    bot.infinity_polling()