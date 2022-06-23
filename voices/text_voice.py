from gtts import gTTS
import mysql.connector
import os

def connect_base(user_name, password, database):
    mydb = mysql.connector.connect(
        host="localhost",
        user=user_name,
        password=password,
        database=database,
    )
    return mydb



mydb = connect_base("root", "", "Golos_Navoiy")
mycursor = mydb.cursor()
mycursor.execute(f"SELECT * FROM mobil_baza")
myresult = mycursor.fetchall()

for i in myresult:
    date = str(i[4])
    mus = gTTS(text = f'sizning axoli punktizga {date} yilda aloqa keladi')
    mus.save(f'{i[2]}_{i[3]}.mp3')
    os.system(f"{i[2]}_{i[3]}.mp3")