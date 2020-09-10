import requests
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types

bot = telebot.TeleBot('1397643322:AAGw6hKb8SVmiRQm4Y2xqsQg1cgHveSuubM')

def usorov(ouname):
    ingliz = 'http://moodle.tdau.uz/course/view.php?id=2852'
    yilqi = 'http://moodle.tdau.uz/course/view.php?id=2667'
    sut = 'http://moodle.tdau.uz/course/view.php?id=2675'
    gostqoramol = 'http://moodle.tdau.uz/course/view.php?id=2676'
    qaytaish = 'http://moodle.tdau.uz/course/view.php?id=2673'
    qoramol = 'http://moodle.tdau.uz/course/view.php?id=2668'
    naslishi = 'http://moodle.tdau.uz/course/view.php?id=2674'
    echki = 'http://moodle.tdau.uz/course/view.php?id=2666'
    try:
        UNAME = ouname
        s = requests.Session()

        # get SCRF
        auth_html = s.get('http://moodle.tdau.uz/')
        auth_bs = BS(auth_html.content, 'html.parser')
        csrf = auth_bs.select('input[name=logintoken]')[0]['value']

        payload = {
            'anchor': '',
            'logintoken': csrf,
            'username': '9217-19',
            'password': 'orzu1997'
        }

        answ = s.post('http://moodle.tdau.uz/login/', data=payload)

        if answ.status_code == 200:
            s.get(ingliz)
            s.get(yilqi)
            s.get(sut)
            s.get(qoramol)
            s.get(qaytaish)
            s.get(gostqoramol)
            s.get(naslishi)
            s.get(echki)
        if answ.status_code == 200:
            sms = 'Ijobiy'
        else:
            sms = 'Salbiy'
    except:
        bot.send_message(message.chat.id, 'SuR BeTan')
    return sms

def sorov(uname):
    ingliz = 'http://moodle.tdau.uz/course/view.php?id=2852'
    yilqi = 'http://moodle.tdau.uz/course/view.php?id=2667'
    sut = 'http://moodle.tdau.uz/course/view.php?id=2675'
    gostqoramol = 'http://moodle.tdau.uz/course/view.php?id=2676'
    qaytaish = 'http://moodle.tdau.uz/course/view.php?id=2673'
    qoramol = 'http://moodle.tdau.uz/course/view.php?id=2668'
    naslishi = 'http://moodle.tdau.uz/course/view.php?id=2674'
    echki = 'http://moodle.tdau.uz/course/view.php?id=2666'
    try:
        UNAME = uname
        s = requests.Session()

        # get SCRF
        auth_html = s.get('http://moodle.tdau.uz/')
        auth_bs = BS(auth_html.content, 'html.parser')
        csrf = auth_bs.select('input[name=logintoken]')[0]['value']
    except:
        bot.send_message(message.chat.id, 'Sur bettan')
    try:
        payload = {
            'anchor': '',
            'logintoken': csrf,
            'username': UNAME,
            'password': 'agrar@2020'
        }
    except:
        bot.send_message(message.chat.id, 'login error')
    try:
        answ = s.post('http://moodle.tdau.uz/login/', data=payload)

        if answ.status_code == 200:
            s.get(ingliz)
            s.get(yilqi)
            s.get(sut)
            s.get(qoramol)
            s.get(qaytaish)
            s.get(gostqoramol)
            s.get(naslishi)
            s.get(echki)
        if answ.status_code == 200:
            sms = 'Ijobiy'
        else:
            sms = 'Salbiy'
    except:
        bot.send_message(message.chat.id, 'Sur bettan dedim')
    return sms

@bot.message_handler(commands=['start','help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("9217-16")
    btn2 = types.KeyboardButton('9217-17')
    btn3 = types.KeyboardButton('9217-18')
    btn4 = types.KeyboardButton("9217-19")
    btn5 = types.KeyboardButton("9217-20")
    btn6 = types.KeyboardButton("9217-21")
    btn7 = types.KeyboardButton("9217-22")
    btn8 = types.KeyboardButton("9217-23")
    btn9 = types.KeyboardButton("9217-24")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    bot.send_message(message.chat.id, message.from_user.first_name, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    uname = ''
    if message.text == '9217-16':
        uname = '9217-16'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-17':
        uname = '9217-17'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-18':
        uname = '9217-18'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-19':
        if message.chat.id == 914886587:
            ouname = '9217-19'
            ums = osorov(ouname)
            bot.send_message(message.chat.id, ums)
    elif message.text == '9217-20':
        uname = '9217-20'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-21':
        uname = '9217-21'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-22':
        uname = '9217-22'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-23':
        uname = '9217-23'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    elif message.text == '9217-24':
        uname = '9217-24'
        sms = sorov(uname)
        bot.send_message(message.chat.id, sms)
    else:
        bot.send_message(message.chat.id, 'KeChiRaSiZ FaRiShta SiZnI TaniMaYDi')

bot.polling(none_stop=True)