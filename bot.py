import telebot
from datetime import datetime
import pytz
import threading
import time

from word import daily_words          # Günlük sözlər
from gram import grammar_lessons      # Günlük qrammatika
from tests import daily_tests         # Günlük testlər

TOKEN = "7962643816:AAFIa0wZ4iVKSCoNO9Jfeuv6m33Uf_77SXY"
CHANNEL_USERNAME = "@farsdersler"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ------------------- START / ANKET -------------------
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📜 Anket", callback_data="anket"))
    bot.send_message(message.chat.id, "**Salam zəhmət olmasa** `Anket` **buttonuna toxunaraq məlumatları doldurun** ✍️", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: call.data=="anket")
def anket(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    msg = bot.send_message(call.message.chat.id, "**Adınız nədir?**")
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    user_name = message.text
    msg = bot.send_message(message.chat.id, "**Yaşınız neçədir?**")
    bot.register_next_step_handler(msg, get_age, user_name)

def get_age(message, user_name):
    user_age = message.text
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton("Bəli", callback_data="yes"),
        InlineKeyboardButton("Xeyr", callback_data="no")
    )
    bot.send_message(message.chat.id, "**Dərslərə qoşulmağa könüllü razısınızmı?**", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: call.data in ["yes","no"])
def lesson_consent(call):
    if call.data == "yes":
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("📚 Dərs Kanalı", url=f"https://t.me/{CHANNEL_USERNAME.strip('@')}"))
        bot.send_message(call.message.chat.id, "**Zəhmət olmasa Dərs Kanalı buttonuna toxunaraq kanala qatılın**", reply_markup=kb)
    else:
        bot.send_message(call.message.chat.id, "**Könüllü razılığınız olmadığı üçün sizi dərs kanalına qata bilməyəcəm**")


# ------------------- GÜNDƏLİK TESTLƏR -------------------
def send_daily_test_poll(day):
    test_list = daily_tests.get(day)
    if not test_list:
        return

    # Suallar üçün vaxtlar
    question_times = ["23:54", "10:00", "12:00", "15:00", "19:00"]

    for idx, (sual_text, variants, correct_index) in enumerate(test_list[:5]):
        hour, minute = map(int, question_times[idx].split(":"))

        # Vaxt gələnə qədər gözlə
        while True:
            now = datetime.now(pytz.timezone("Asia/Baku"))
            if now.hour == hour and now.minute == minute:
                bot.send_poll(
                    chat_id=CHANNEL_USERNAME,
                    question=f"{idx+1}. {sual_text}",
                    options=variants,
                    is_anonymous=False,
                    type="quiz",
                    correct_option_id=correct_index
                )
                break
            time.sleep(5)


# ------------------- GÜNDƏLİK MƏZMUN GÖNDƏRİM -------------------
def send_daily_content():
    days = list(daily_words.keys())
    current_day_index = 0
    sent_flags = {}

    while current_day_index < len(days):
        now = datetime.now(pytz.timezone("Asia/Baku"))
        hour, minute = now.hour, now.minute
        day = days[current_day_index]

        if day not in sent_flags:
            sent_flags[day] = {"words": False, "grammar": False, "test": False}

        # ---- SÖZLƏR ----
        if not sent_flags[day]["words"] and hour == 8 and minute == 0:
            words = daily_words[day]
            text = f"📖 {day} - **Günün sözləri:**\n"
            for w in words:
                text += f"{w[0]} • {w[1]} • {w[2]}\n"
            bot.send_message(CHANNEL_USERNAME, text=text)
            sent_flags[day]["words"] = True

        # ---- QRAMMATİKA ----
        if not sent_flags[day]["grammar"] and hour == 13 and minute == 0:
            lesson = grammar_lessons.get(day)
            if lesson:
                text = f"📚 {day} - **Gündəlik Qrammatika** ({lesson['ders']}):\n{lesson['izah']}\nNümunə: {lesson['nümunə']}"
                bot.send_message(CHANNEL_USERNAME, text=text)
            sent_flags[day]["grammar"] = True

        # ---- TEST ----
        if not sent_flags[day]["test"]:
            threading.Thread(target=send_daily_test_poll, args=(day,)).start()
            sent_flags[day]["test"] = True

        # Gün sonu
        if hour == 0 and minute == 0:
            current_day_index += 1

        time.sleep(20)


# ------------------- THREAD -------------------
threading.Thread(target=send_daily_content).start()

# ------------------- BOT POLLING -------------------
bot.infinity_polling()
