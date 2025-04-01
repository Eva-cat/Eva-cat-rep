import os
import telebot

API_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я Єва — твоя AI-помічниця.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Єва ще не навчена цьому, але я вже вчуся!")

bot.polling()
