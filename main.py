#импорт_библиотек
import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI

#токен_бота
bot = telebot.TeleBot('5403689922:AAHSUaX-PVFd60oeM093FuJwbQpidr6Cdgk')

#получение_курсов
cg = CoinGeckoAPI()

#---------------------------------------------------------------------------------
#начальное_состояние
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    #положение_кнопок_на_превой_строке
    markup.row("/Currency")
    #положение_кнопок_на_второй_строке
    markup.row("/Rbc", "/Izvestia", "/Finam", "/1Prime", "/Lenta")
    #положение_кнопок_на_третьей_строке
    markup.row("/help")

    #имя_пользователя
    f_name = message.from_user.first_name
    #фамилия_пользователя
    l_name = message.from_user.last_name

    #проверка_имени_пользователя
    if (f_name and l_name):
        user_name = f'<b>{f_name} <u>{l_name}</u></b>'
    elif (f_name and l_name == None):
        user_name = f'<b>{f_name}</b>'
    elif (f_name == None and l_name):
        user_name = f'<b>{l_name}</b>'
    else:
        user_name = f'<b>Неизвестный гость</b>'

    #приветственное_сообщение
    bot.send_message(message.chat.id,
                    f"<b>CryptoBot, приветствует Вас \n{user_name}</b>",
                    parse_mode='html')
    #предложение_на_выбор_пункта_меню
    bot.send_message(message.chat.id,
                    "<b>Выберите, пожалуйста, пункт меню: </b>",
                    parse_mode='html',
                    reply_markup=markup)

#---------------------------------------------------------------------------------
#функция_справки
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
        "/help - команды, которые я могу выполнить \n"
        "/Rbc, /Ria, /Finam, /1Prime, /Lenta - \n"
        "ссылки на новостные порталы: \n"
        "Rbc, Ria, Finam, 1Prime, Lenta \n"
        "\n"
        "/Currency - значения котировок по валютным парам: \n"
        "Bitcoin/USD, Monero/USD, Litecoin/USD, Ethereum/USD")

#---------------------------------------------------------------------------------
#RBC_channel
@bot.message_handler(commands=['Rbc'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://www.rbc.ru/crypto/')

#RIA_channel
@bot.message_handler(commands=['Izvestia'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://www.iz.ru/tag/kriptovaliuta/')

#FINAM_channel
@bot.message_handler(commands=['Finam'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://www.finam.ru/publications/section/cryptonews/')

#1Prime_channel
@bot.message_handler(commands=['1Prime'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://www.1prime.ru/trend/bitcoins/')

#LENTA_channel
@bot.message_handler(commands=['Lenta'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://www.lenta.ru/rubrics/economics/crypto/')

#---------------------------------------------------------------------------------
#получение_значения_для_пары_BTC/USD
@bot.message_handler(commands=['Currency'])
def get_course(message):
    course = cg.get_price(ids='bitcoin', vs_currencies='usd')
    curr = bot.reply_to(message, text=f"Bitcoin ${course['bitcoin']['usd']:.2f}")
    course = cg.get_price(ids='monero', vs_currencies='usd')
    curr = bot.reply_to(message, text=f"Monero ${course['monero']['usd']:.2f}")
    course = cg.get_price(ids='litecoin', vs_currencies='usd')
    curr = bot.reply_to(message, text=f"Litecoin ${course['litecoin']['usd']:.2f}")
    course = cg.get_price(ids='ethereum', vs_currencies='usd')
    curr = bot.reply_to(message, text=f"Ethereum ${course['ethereum']['usd']:.2f}")

#---------------------------------------------------------------------------------
#запуск_бота
bot.polling(none_stop = True)




