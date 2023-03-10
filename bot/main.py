import telebot
from telebot import types
from config import TOKEN, TELEGRAM_URL


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    file = open('199032326.jpg', 'rb')
    bot.send_photo(message.chat.id, file)

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(text='BYBIT')
    button2 = types.KeyboardButton(text='MEXC')
    button3 = types.KeyboardButton(text='HUOBI')
    button4 = types.KeyboardButton(text='BITGET')
    button5 = types.KeyboardButton(text='PHEMEX')
    button6 = types.KeyboardButton(text='BINANCE')

    kb.add(button1, button2)
    kb.add(button3, button4)
    kb.add(button5, button6)
    bot.send_message(message.chat.id, 'Вступай в группу ' + TELEGRAM_URL)
    bot.send_message(message.chat.id, 'Ниже кнопки с регистрацией самых перспективных и быстроразвивающих бирж в 2023 году!', reply_markup=kb)

@bot.message_handler(func=lambda x: x.text == 'BYBIT')
def set_url1(message):
    bot.reply_to(message, 'Cамая народная и с суперакциями и розыгрышами \n\n https://www.bybit.com/ru-RU/invite?ref=Y6QXZY')

@bot.message_handler(func=lambda x: x.text == 'MEXC')
def set_url2(message):
    bot.reply_to(message, 'самая безопасная биржа MEXC \n\n https://www.mexc.com/register?inviteCode=1XsVk')

@bot.message_handler(func=lambda x: x.text == 'HUOBI')
def set_url3(message):
    bot.reply_to(message, 'Самая инновационная биржа HUOBI \n\n https://www.huobi.com/ru-ru/v/register/double-invite/?invite_code=rswe4223&inviter_id=11345710')

@bot.message_handler(func=lambda x: x.text == 'BITGET')
def set_url4(message):
    bot.reply_to(message, 'Самая лояльная к СНГ коммьюнити  BITGET \n\n https://www.bitget.com/ru/referral/register?from=referral&clacCode=HKU36WKG')

@bot.message_handler(func=lambda x: x.text == 'PHEMEX')
def set_url5(message):
    bot.reply_to(message, 'Самая быстрорастущая биржа \n\n Я торгую криптовалютой на Phemex.Присоединяйтесь ко мне и получите эксклюзивный бонус в BTC \n https://phemex.com/register?platform=app&referralCode=G242X4')

@bot.message_handler(func=lambda x: x.text == 'BINANCE')
def set_url6(message):
    bot.reply_to(message, 'Самая известная и щедрая биржа на бонусы \n\n  https://www.binance.com/ru/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00OU20Q5SB')

if __name__ == "__main__":
    bot.polling()

