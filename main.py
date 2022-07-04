# from email import message
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
from conf import Start_command, bot, Documentation
import mysql.connector
import datetime
import nltk
import random
from gtts import gTTS
import requests


start = Start_command()
document = Documentation()


def k_or_l(text):

    a = random.randint(0,len(text)-1)
    b = random.randint(0,len(text)-1)
    c = random.randint(0,len(text)-1)
    d = random.randint(0,len(text)-1)
    # print(text[a],text[b],text[c],text[d])
    if ( 65 >= ord(text[a]), ord(text[b]), ord(text[c]), ord(text[d]) >= 122 ):
        return 1
    else:
        return 0

def replace_def(text):
    if k_or_l(text) == 1:
        dict_replace = {
            "A":{'lotin': 'A','kiril':'А'},
            "a":{'lotin': 'a','kiril':'а'},
            
            'Sh':{"lotin":"Sh", "kiril":'Ш'},
            'sh':{"lotin":"sh", "kiril":'ш'},
            
            'SH':{"lotin":"SH", "kiril":'Ш'},

            "B":{'lotin': 'B', "kiril": 'Б'},
            "b":{"lotin": 'b', 'kiril':'б'},
            
            "ch":{'lotin': 'ch', 'kiril':'ч'},
            "Ch":{'lotin':'Ch','kiril':'Ч'},

            "CH":{'lotin':'CH','kiril':'Ч'},
            
            "D":{'lotin':'D', "kiril":'Д'},
            "d":{"lotin":'d', 'kiril':'д'},
            
            'E':{'lotin':'E', 'kiril':'Е'},
            'e':{"lotin": 'e', 'kiril':'е'},
            
            'F':{"lotin":"F", "kiril":'Ф'},
            'f':{"lotin": 'f', 'kiril':'ф'},
            
            'G':{"lotin":"G", "kiril":'Г'},
            'g':{"lotin": 'g', 'kiril':'г'},
            
            'H':{"lotin":"H", "kiril":'Ҳ'},
            'h':{"lotin":'h', 'kiril':'ҳ'},
            
            'I':{"lotin":"I", "kiril":'И'},
            'i':{"lotin": 'i', 'kiril':'и'},
            
            'J':{"lotin":"J", "kiril":'Ж'},
            'j':{"lotin":'j', 'kiril':'ж'},
            
            'K':{"lotin":"K", "kiril":'К'},
            'k':{"lotin": 'k', 'kiril':'к'},
            
            'L':{"lotin":"L", "kiril":'Л'},
            'l':{"lotin": 'l', 'kiril':'л'},
            
            'M':{"lotin":"M", "kiril":'М'},
            'm':{"lotin": 'm', 'kiril':'м'},
            
            'N':{"lotin":"N", "kiril":'Н'},
            'n':{"lotin": 'n', 'kiril':'н'},
            
            'O':{"lotin":"O", "kiril":'О'},
            'o':{"lotin": 'o', 'kiril':'о'},
            
            "O'":{"lotin":"O'", "kiril":'Ў'},
            "o'":{"lotin": "o'", 'kiril':'ў'},
            
            'P':{"lotin":"P", "kiril":'П'},
            'p':{"lotin": 'p', 'kiril':'п'},
            
            'Q':{"lotin":"Q", "kiril":'Қ'},
            'q':{"lotin":"q", "kiril":'қ'},
            
            'R':{"lotin":"R", "kiril":'Р'},
            'r':{"lotin":"r", "kiril":'р'},
            
            'S':{"lotin":"S", "kiril":'С'},        
            's':{"lotin":"s", "kiril":'с'},
            
        
            
            'T':{"lotin":"T", "kiril":'Т'},
            't':{"lotin":"t", "kiril":'т'},
            
            'U':{"lotin":"U", "kiril":'У'},
            'u':{"lotin":"u", "kiril":'у'},

            'V':{"lotin":"V", "kiril":'В'},
            'v':{"lotin":"v", "kiril":'в'},
            
            'X':{"lotin":"X", "kiril":'Х'},
            'x':{"lotin":"x", "kiril":'х'},

            'Y':{"lotin":"Y", "kiril":'Й'},
            'y':{"lotin":"y", "kiril":'й'},
            
            'Z':{"lotin":"Z", "kiril":'З'},
            'z':{"lotin":"z", "kiril":'з'},

            "G'":{"lotin":"G'", "kiril":'Ғ'},
            "g'":{"lotin":"g'", "kiril":'ғ'},
        }
        for item in dict_replace:
            #print(dict_replace[str(item)]['lotin'],dict_replace[str(item)]['kiril'])
            text = text.replace(str(dict_replace[str(item)]['lotin']),str(dict_replace[str(item)]['kiril']))
        return text
    else:
        print('kirilcha')    
   
  


def connect_to_base(user, password, database):
    mydb = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database=database,
    )
    return mydb


def sacn_opr(message):
        mydb = connect_to_base("root", "", "Golos_Navoiy")

        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM users where User_id = {str(message.chat.id)}")
        myresult = mycursor.fetchall()
        print('do myresult')
        
        for i in myresult:
            if i[5] == 'operator':
                mycursor_i = mydb.cursor()
                mycursor_i.execute("SELECT a.user_id, a.application, a.app_type,a.id, u.User_id, u.fio From application a, users u WHERE a.user_id = u.User_id")
                myresult_i = mycursor_i.fetchall()

                for y in myresult_i:
                    print(y)
                    if y[2] == 'new':
                            print('new')
                            user_app = y[1]
                            user_name = i[4]
                            post_id = y[2]
                                
                                
                            keyboard = InlineKeyboardMarkup(row_width = 1)
                            button1 = InlineKeyboardButton(text=user_name, callback_data=f'post{post_id}')

                            keyboard.add(button1)

                            bot.send_message(message.chat.id, text=user_app, reply_markup=keyboard)
            elif i[5] == 'user':
                print(i[5])
                asd = message.chat.id
                start.create_post(asd)





def scan_user(message):
    mydb = connect_to_base("root", "", "Golos_Navoiy")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT count(*) FROM users where User_id = {str(message.chat.id)}")
    myresult = mycursor.fetchone()
    if myresult[0] <= 0:
        print('Здесь все работает')
        start.create_button(message)

    else:
        bot.send_message(message.chat.id, 'siz registraciyadan alla qachon utgan siz')
        sacn_opr(message)
       # start.create_post(message.chat.id)



def add_app(id):
    mydb = connect_to_base("root","","Golos_Navoiy")
    mycursor = mydb.cursor()
    applicate = document.users_aplication[str(id)]
    print(document.users_aplication)
    t_day = datetime.date.today()   
    region_sql = "SELECT DISTINCT(Tuman) FROM mobil_baza"
    mycursor.execute(region_sql)
    my_regions = mycursor.fetchall()
    if applicate['button'] == 'Aloqa':
  
        for item in my_regions:
            phraz = replace_def(applicate['application']).lower() 
            phraz_i = phraz.split()
            

            for phraz_item in phraz_i:
                if len(phraz_item) > len(item[0]):
                    distance = nltk.edit_distance(item[0],phraz_item)/len(phraz_item)
                else:
                    distance = nltk.edit_distance(item[0],phraz_item)/len(item)

                if distance <= 0.3:
                    my_find = phraz_item
                    bot.send_message(id,f"naydena fraza {my_find}")
                    
                    mycursor_s = mydb.cursor()
                    axoli_sql = f"SELECT * FROM mobil_baza WHERE Tuman = '{my_find}'"
                    mycursor_s.execute(axoli_sql)
                    punkts = mycursor_s.fetchall()
                    
                    for for_punkst in punkts:

                        for item_phraz in phraz_i:

                            for_punkts_s = for_punkst[3]


                            if len(item_phraz) > len(for_punkts_s[0]):
                                distance_punkt = nltk.edit_distance(for_punkts_s,item_phraz)/len(item_phraz)
                            else:
                                distance_punkt = nltk.edit_distance(for_punkts_s,item_phraz)/len(for_punkts_s)

                            if distance_punkt <= 0.2:
                                my_reg = item_phraz
                                bot.send_message(id,f"naydena fraza {my_reg}")


                                mycursor_s = mydb.cursor()
                                axoli_sql = f"SELECT * FROM mobil_baza WHERE Tuman = '{my_find}' and Axoli_punkt = '{my_reg}'"
                                mycursor_s.execute(axoli_sql)
                                my_reg_find = mycursor_s.fetchall()
                                for i in my_reg_find:

                                    date = str(for_punkst[4])
                                    # mus = gTTS(text = f'sizning axoli punktizga {date} yilda aloqa keladi')
                                    mus  = gTTS(text = f'сизнинг ахоли пунктизда {date} йилида алока келади', lang = 'ru')
                                    mus.save(f'{for_punkst[2]}_{for_punkst[3]}.mp3')
                                    
                                    aud = open(f"{for_punkst[2]}_{for_punkst[3]}.mp3", "rb")
                                    bot.send_audio(id, aud)
                else:
                    mydb = connect_to_base("root","","Golos_Navoiy")
                    mycursor_a = mydb.cursor()
                    sql = 'INSERT INTO application(user_id, application, date, app_button) VALUES (%s, %s, %s, %s)'
                    val = (str(id), applicate['application'],t_day, applicate['button'])
                    mycursor_a.execute(sql, val)
                    mydb.commit()    
                    document.clear_item()
                    bot.send_message(id, 'sizning arizangizga yaqin orada javob beriladi')


    elif applicate['button'] == 'Boshqa...':
        mydb = connect_to_base("root","","Golos_Navoiy")
        mycursor_b = mydb.cursor()
        sql = 'INSERT INTO application(user_id, application, date, app_button) VALUES (%s, %s, %s, %s)'
        val = (str(id), applicate['application'],t_day, applicate['button'])
        mycursor_b.execute(sql, val)
        mydb.commit()    
        document.clear_item()
        bot.send_message(id, 'sizning arizangizga yaqin orada javob beriladi')
    elif applicate['button'] == 'Internet':
        pass


    print("clear function")
    document.clear_item()


                            

                            
                        

                            # """
                            # mycursor_s = mydb.cursor()
                            # axoli_sql = f"SELECT DISTINCT(Axoli_punkt) FROM mobil_baza WHERE Tuman = '{my_find}'"
                            # mycursor_s.execute(axoli_sql)
                            # punkts = mycursor_s.fetchall()"""
                            
                    # if punkts == phraz_i:
                # bot.send_message(id, f"{punkts} == {phraz_i}")
                
                # """
                #     if len(phraz_item) > len(axoli_p):
                #         distance_punkt = nltk.edit_distance(axoli_p[0],phraz_item)/len(phraz_item)
                #         print(f'{phraz_item} > {axoli_p[0]}')
                #         bot.send_message(id, f'{phraz_item} > {axoli_p[0]}')

                #     else:
                #         distance = nltk.edit_distance(axoli_p[0],phraz_item)/len(axoli_p)

                #     if distance_punkt <= 0.4:
                #         bot.send_message(id, f"Найдена фраза {phraz_item}") 

                #     else:
                #         bot.send_message(id,f"Дистанция {distance}")                   
                # """
    # if ('Konimex' == applicate['application'] or distance <= 0.2):
    #     bot.send_message(id,f" Sizni suxbatdoshiz  {distance} ")
    # else:
    #     bot.send_message(id,distance)


def add_user(id):
    mydb = connect_to_base("root", "", "Golos_Navoiy")
    mycursor = mydb.cursor()
    user = start.users_info[str(id)]
    sql = f"INSERT INTO users(User_id, fio, Phone, Adres, types ) VALUES ( '{id}' ,'{user['fio']}' , '{user['phone']}', '{user['adres']}', 'user')"
    mycursor.execute(sql)
    mydb.commit()
    start.clear_user()


def add_fio(message):
    if len(message.text) >=8:
        start.add_fio(message.text, message.chat.id)
        check_user(message.chat.id)
        asd = 'sizning FIO qabul qilindi'
        bot.send_message(message.chat.id, asd)
    else:
        bot.send_message(message.chat.id, '⁉️ ⁉️ ⁉️ Iltimos FIO tugmasini qaytib bosing va ismingizni toliq kiriting')

def add_phone(message):
    start.add_phone(message.contact.phone_number, message.chat.id)
    check_user(message.chat.id)
    print(start.users_info)
    asd = 'sizning telefon qabul qilindi'
    bot.send_message(message.chat.id, asd)


def add_adres(message):
    start.add_adres(message.text, message.chat.id)
    check_user(message.chat.id)
    asd = 'sizning adres qabul qilindi'
    bot.send_message(message.chat.id, asd)

def otvet_na_vopros_opr(message,*id):
    if message.content_type == 'text':
        mydb = connect_to_base("root", "", "Golos_Navoiy")
        mycursor = mydb.cursor()
        id = str(*id)
        sql = f"UPDATE application SET answer_aplicate = '{message.text}', app_type = 'reviewed' WHERE id ={id[4:]}"
        mycursor.execute(sql)
        mydb.commit()
        send_sql = f"select * from application where id = {id[4:]}"
        mycursor.execute(send_sql)
        res = mycursor.fetchone()
        bot.send_message(message.chat.id, 'sizning javobingiz qabul qilindi')
        bot.send_message(res[1],f"Sizning '{res[2]}' murojaatingizga javoban '{res[3]}'")
    elif message.content_type == 'document':
        dok_name = message.document.file_name
        file_id = bot.get_file(message.document.file_id).file_path
        download_doc = bot.download_file(file_id)
        safe_src = "files/" + f'{dok_name}'
        with open(safe_src, "wb") as save_file:
            save_file.write(download_doc)
        bot.send_message(message.chat.id, 'Dokument instaling...')


        mydb = connect_to_base("root", "", "Golos_Navoiy")
        mycursor = mydb.cursor()
        id = str(*id)
        sql = f"UPDATE application SET answer_doc = '{safe_src}', app_type = 'review' WHERE id ={id[4:]}"
        mycursor.execute(sql)
        mydb.commit()
        send_sql = f"select * from application where id = {id[4:]}"
        mycursor.execute(send_sql)
        res = mycursor.fetchone()
        bot.send_message(message.chat.id, 'sizning faylingiz qabul qilindi')
        bot.send_message(res[1],f"Sizning '{res[2]}' murojaatingizga javoban")
        doc = open(safe_src, 'rb')
        bot.send_document(res[1], doc)
        





def safe_document(message):
    print(message)
    dok_name = message.document.file_name
    file_id = bot.get_file(message.document.file_id).file_path
    download_doc = bot.download_file(file_id)
    safe_src = "files/" + f"{dok_name}"
    with open(safe_src, "wb") as save_file:
        save_file.write(download_doc)
    bot.send_message(message.chat.id, 'Dokument instaling')

    






def check_user(id):
    user = start.get_user(id)
    my_keys = list(user.keys())
    print(my_keys)
    if "fio" in my_keys and "adres" in my_keys and "phone" in my_keys:
        if (len(user["fio"]) > 5 and len(user["phone"]) > 10 and len(user["adres"]) > 5):
            bot.send_message(id, "Siz registratsiyadan to'liq o'tdiz endi ma'lumot junatsangiz ham bo'ladi!")
            start.create_post(id)
            add_user(id)



def check_application(id):
    applicate = document.get_app(id)
    my_keys = list(applicate.keys())
    if "application" in my_keys:
        if len(applicate['application'])>4:
            add_app(id)
            asd = '✅ sizning arizangiz qabul qilindi!\n1️⃣Sizning arizangiz birinchi bosqichda...'
            bot.send_message(id, asd)
    


def ariza_vopros(message):
    document.add_chat_id(message.chat.id)
    document.add_applicatiio(message.text, message.chat.id)
    check_application(message.chat.id)
    





def admin_wath(message):
    mydb = connect_to_base("root", "", "Golos_Navoiy")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT count(*) FROM application where user_id = {str(message.chat.id)}")
    myresult = mycursor.fetchone()
    for i in myresult:
        if i[4] == 'new':
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT count(*) FROM users")
            myresult_Y = mycursor.fetchone()
            for y in myresult_Y:
                keyboard = InlineKeyboardMarkup()
                button1 = InlineKeyboardButton(text=y[1], callback_data=y[1])
                keyboard.add(button1)
                bot.send_message(message.chat.id, text=i[2], reply_markup=keyboard)
            


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if (message.text == '/start'):
        start.add_chat_id(message.chat.id)
        scan_user(message)

@bot.message_handler(content_types=['text'])
def button_processing(message):
    if message.text == 'Aloqa' or message.text == 'Boshqa...' or message.text == 'Internet':
        asd = 'iltimos qiynagan savolingizni bravering, yaqin orada biz javob berishga harakat qilamiz'
        bot.send_message(message.from_user.id, asd,reply_markup=telebot.types.ReplyKeyboardRemove())
        document.add_chat_id(message.chat.id)
        document.add_button(message.text, message.chat.id)
        check_application(message.chat.id)
        bot.register_next_step_handler(message, ariza_vopros)    



@bot.callback_query_handler(func=lambda call: True)
def inline_answer(call):
    if (call.data == 'fio'):
        bot.send_message(call.from_user.id, "FIO kiriting!")
        bot.register_next_step_handler(call.message, add_fio)
    elif (call.data == 'tel'):
        name = call.from_user.first_name
        asd = f'{name} telefon raqamingizni bilan bulishing!'
        keyboard = ReplyKeyboardMarkup()
        button = KeyboardButton(text='Nomer telefoni tashash', request_contact=True)
        keyboard.add(button)
        bot.send_message(call.from_user.id, text=asd, reply_markup=keyboard)
    elif (call.data == 'adres'):
        bot.send_message(call.from_user.id, "Adresni kiriting!")
        bot.register_next_step_handler(call.message, add_adres)
    elif call.data == 'xakim':
        pass
    elif call.data == 'ariza':

        asd = 'iltimos muamoni turini tanlang:'

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        key_1 = types.KeyboardButton(text="Aloqa")
        key_2 = types.KeyboardButton(text="Internet")
        key_3 = types.KeyboardButton(text="Boshqa...")
        keyboard.add(key_1, key_2, key_3)
        bot.send_message(call.from_user.id, asd, reply_markup=keyboard)

        
        

        
    elif call.data[:4] == 'post':
        bot.send_message(call.from_user.id, 'Shu savolga javobini yozing')
        bot.register_next_step_handler(call.message, otvet_na_vopros_opr,call.data)
        #bot.register_next_step_handler(call.message, safe_document)



        
@bot.message_handler(content_types=['contact'])
def number_user(message):
    add_phone(message)






bot.polling()
