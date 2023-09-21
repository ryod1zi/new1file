import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot_token = '6617791957:AAHNwJz6AJuM6FWRXg9hZe_v5Hd0y6VZK7o'

bot = telebot.TeleBot(bot_token)

news_data = []

@bot.message_handler(commands=['start'])
def start(message):
    parse_news()
    
    send_news_list(message.chat.id)
def parse_news():
    global news_data
    news_data = []

    url = 'https://kaktus.media/?lable=8&date=2023-09-21&order=time'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('div', class_='Tag--article')
    print(url)
    for i, news in enumerate(news_items[:20], 1):
        title = news.text.strip()
        news_data.append({"id": i, "title": title})
def send_news_list(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for news in news_data:
        markup.add(types.KeyboardButton(str(news["id"])))
    
    bot.send_message(chat_id, "Выберите номер новости (1-20):", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_numeric_selection(message):
    news_id = int(message.text)

    selected_news = next((news for news in news_data if news["id"] == news_id), None)

    if selected_news:
        send_news_description(message.chat.id, selected_news)
    else:
        bot.send_message(message.chat.id, "Новость не найдена")

def send_news_description(chat_id, news):
    description = "Описание новости отсутствует"  

    bot.send_message(chat_id, f"{news['title']}:\n\n{description}")

@bot.message_handler(func=lambda message: not message.text.isdigit())
def handle_non_numeric_selection(message):
    bot.send_message(message.chat.id, "Пожалуйста, введите номер новости (число)")

if __name__ == "__main__":
    bot.polling(none_stop=True) 






