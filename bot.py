import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import pytz
import threading
import time

# Fayllardan məlumatları import edirik
from word import daily_words
from gram import grammar_lessons
from tests import daily_tests

TOKEN = "7962643816:AAFIa0wZ4iVKSCoNO9Jfeuv6m33Uf_77SXY"
CHANNEL_USERNAME = "@farsdersler"  # Kanala mesaj göndərmək üçün username
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ---- START / ANKET ----
@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📜 Anket", callback_data="anket"))
    bot.send_message(message.chat.id, "Salam zəhmət olmasa Anket buttonuna toxunaraq məlumatları doldurun ✍️", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: call.data=="anket")
def anket(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    msg = bot.send_message(call.message.chat.id, "Adınız nədir?")
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    user_name = message.text
    msg = bot.send_message(message.chat.id, "Yaşınız neçədir?")
    bot.register_next_step_handler(msg, get_age, user_name)

def get_age(message, user_name):
    user_age = message.text
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton("Bəli", callback_data="yes"),
        InlineKeyboardButton("Xeyr", callback_data="no")
    )
    bot.send_message(message.chat.id, "Dərslərə qoşulmaqa könüllü razısınızmı?", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: call.data in ["yes","no"])
def lesson_consent(call):
    if call.data == "yes":
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("📚 Dərs Kanalı", url=f"https://t.me/{CHANNEL_USERNAME.strip('@')}"))
        bot.send_message(call.message.chat.id, "Zəhmət olmasa Dərs Kanalı buttonuna toxunaraq kanala qatılın", reply_markup=kb)
    else:
        bot.send_message(call.message.chat.id, "Könüllü razılığınız olmadığı üçün sizi dərs kanalına qata bilməyəcəm")

# ---- FUNKSİYALAR: GÜNÜN SÖZLƏRİ, QRAMMATİKA, TEST ----
def send_daily_content():
    posted_days = set()  # Hansı günlər göndərilib
    while True:
        now = datetime.now(pytz.timezone("Asia/Baku"))
        hour = now.hour
        minute = now.minute

        for day in daily_words.keys():
            if day not in posted_days:
                # Səhər 08:00 - sözlər
                if hour == 22 and minute == 45:
                    words = daily_words[day]
                    text = f"📖 {day} - Günün sözləri:\n"
                    for w in words:
                        text += f"{w[0]} • {w[1]} • {w[2]}\n"  # tuple üçün dəyişiklik
                    bot.send_message(CHANNEL_USERNAME, text=text)

                # Günorta 13:00 - qrammatika
                if hour == 22 and minute == 46:
                    lesson = grammar_lessons.get(day)
                    if lesson:
                        text = f"📚 {day} - Gündəlik Qrammatika ({lesson['ders']}):\n{lesson['izah']}\nNümunə: {lesson['nümunə']}"
                        bot.send_message(CHANNEL_USERNAME, text=text)

                # Gecə 19:00 - test
                if hour == 22 and minute == 47:
                    test = daily_tests.get(day)
                    if test:
                        text = f"📝 {day} - Günün Testi:\n"
                        for idx, q in enumerate(test['sual'],1):
                            text += f"{idx}. {q}\n"
                        bot.send_message(CHANNEL_USERNAME, text=text)

                # Gecə 21:00 - cavablar
                if hour == 22 and minute == 48:
                    test = daily_tests.get(day)
                    if test:
                        text = f"✅ {day} - Test Cavabları:\n"
                        for idx, a in enumerate(test['cavab'],1):
                            text += f"{idx}. {a}\n"
                        bot.send_message(CHANNEL_USERNAME, text=text)
                    posted_days.add(day)

        time.sleep(20)  # 20 saniyə gecikmə

# ---- THREAD ----
threading.Thread(target=send_daily_content).start()

# ---- BOT POLLING ----
bot.infinity_polling()
