from email.mime import application
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import mysql.connector


TOKEN = '5258731086:AAG4DQtmKUWN0NZ8durH9Dq6RrISYLlAWI4'
bot = telebot.TeleBot(TOKEN)

users = {}
applikation = {}


class Start_command:
    users = []
    users_info = {}

    def __init__(self):
        self.chat_id = ""
        self.fio = ""
        self.adres = ""
        self.phone = ""

    def add_chat_id(self, chat_id):
        if chat_id not in Start_command.users:
            Start_command.users.append(chat_id)
            Start_command.users_info = {str(chat_id): {}}
        self.chat_id = chat_id

    def add_fio(self, fio, chat_id):
        if chat_id in Start_command.users:
            Start_command.users_info[str(chat_id)].update(fio=fio)
        return self.__dict__

    def add_adres(self, adres, chat_id):
        if chat_id in Start_command.users:
            Start_command.users_info[str(chat_id)].update(adres=adres)        
        return self.__dict__

    def add_phone(self, phone, chat_id):
        if chat_id in Start_command.users:
            Start_command.users_info[str(chat_id)].update(phone=phone)
        return self.__dict__

    def get_user(self, chat_id):
        return Start_command.users_info[str(chat_id)]

    def clear_user(self):
        self.chat_id = ""
        self.fio = ""
        self.phone = ""
        self.adres = ""

    def __str__(self):
        return users

    def create_button(self, message):
        name = message.from_user.first_name
        abs = f'Salom {name} botga xush kelibsiz'
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text="Familiya Ism", callback_data="fio")
        button2 = InlineKeyboardButton(text="Telefon", callback_data="tel")
        button3 = InlineKeyboardButton(text="Adres", callback_data="adres")
        keyboard.add(button1, button2, button3)
        bot.send_message(message.chat.id, text=abs, reply_markup=keyboard)

    def create_post(self, id):
        keyboard = InlineKeyboardMarkup(row_width = 1)
        button1 = InlineKeyboardButton(text="Ariza berish", callback_data="ariza")
        button2 = InlineKeyboardButton(text="Xokimlik xaqida", callback_data='xakim')
        button3 = InlineKeyboardButton(text = "Bot xaqida m'alumot", callback_data='ifo_bot')
        keyboard.add(button1, button2, button3)
        bot.send_message(id, text="Bironta amalni tanlang!", reply_markup=keyboard)

   
    
    

class Documentation:
    applikation = []
    users_aplication = {}

    def __init__(self):
        self.chat_id = ""
        self.application = ""


    def add_chat_id(self, chat_id):
        if chat_id not in Documentation.applikation:
            Documentation.applikation.append(chat_id)
            Documentation.users_aplication = {str(chat_id): {}}
        self.chat_id = chat_id

    def add_applicatiio(self, application, chat_id):
        if chat_id in Documentation.applikation:
            Documentation.users_aplication[str(chat_id)] = {'application':application}
        return self.__dict__

    def get_app(self, chat_id):
        return Documentation.users_aplication[str(chat_id)]

    def clear_item(self):
        self.chat_id = ""
        self.application = ""

    def __str__(self):
        return applikation
    
