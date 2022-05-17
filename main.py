import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from conf import Start_command, bot, Documentation
import mysql.connector
import datetime


start = Start_command()
document = Documentation()






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
                mycursor_i.execute("SELECT * FROM application")
                myresult_i = mycursor_i.fetchall()

                for y in myresult_i:
                    print(y)
                    if y[6] == 'new':
                            print('new')
                            user_app = y[2]
                            user_name = str(i[1])
                            post_id = y[0]
                                
                                
                            keyboard = InlineKeyboardMarkup(row_width = 1)
                            button1 = InlineKeyboardButton(text=user_name, callback_data=f'post{post_id}')

                            keyboard.add(button1)

                            bot.send_message(message.chat.id, text=user_app, reply_markup=keyboard)
            elif i[5] == 'user':
                print(i[5])
                start.create_post(message)





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
    t_day = datetime.date.today()
    print(applicate)
    sql = 'INSERT INTO application(user_id, application, date) VALUES (%s, %s, %s)'
    val = (str(id), applicate['application'],t_day)
    mycursor.execute(sql, val)
    mydb.commit()
    print(sql)
    document.clear_item()



def add_user(id):
    mydb = connect_to_base("root", "", "Golos_Navoiy")
    mycursor = mydb.cursor()
    user = start.users_info[str(id)]
    sql = f"INSERT INTO users(User_id, fio, Phone, Adres, types ) VALUES ( '{id}' ,'{user['fio']}' , '{user['phone']}', '{user['adres']}', 'user')"
    mycursor.execute(sql)
    mydb.commit()
    start.clear_user()


def add_fio(message):
    start.add_fio(message.text, message.chat.id)
    print(start.users_info)
    check_user(message.chat.id)
    asd = 'sizning FIO qabul qilindi'
    bot.send_message(message.chat.id, asd)


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
        sql = f"UPDATE application SET answer_aplicate = '{message.text}', app_type = 'review' WHERE id ={id[4:]}"
        mycursor.execute(sql)
        mydb.commit()
        send_sql = f"select * from application where id = {id[4:]}"
        mycursor.execute(send_sql)
        res = mycursor.fetchone()
        bot.send_message(message.chat.id, 'sizning javobingiz qabul qilindi')
        bot.send_message(res[1],f"Sizning {res[2]} murojaatingizga javoban {res[3]}")
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
        bot.send_message(res[1],f"Sizning {res[2]} murojaatingizga javoban")
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
        if (len(user["fio"]) > 7 and len(user["phone"]) > 10 and len(user["adres"]) > 5):
            bot.send_message(id, "Siz registratsiyadan to'liq o'tdiz endi ma'lumot junatsangiz ham bo'ladi!")
            start.create_post(id)
            add_user(id)



def check_application(id):
    applicate = document.get_app(id)
    my_keys = list(applicate.keys())
    if "application" in my_keys:
        if len(applicate['application'])>20:
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
        asd = 'iltimos qiynagan savolingizni bravering, yaqin orada biz javob berishga harakat qilamiz'
        bot.send_message(call.from_user.id, asd)
        bot.register_next_step_handler(call.message, ariza_vopros)
    elif call.data[:4] == 'post':
        bot.send_message(call.from_user.id, 'Shu savolga javobini yozing')
        bot.register_next_step_handler(call.message, otvet_na_vopros_opr,call.data)
        #bot.register_next_step_handler(call.message, safe_document)



        
@bot.message_handler(content_types=['contact'])
def number_user(message):
    add_phone(message)






bot.polling()
