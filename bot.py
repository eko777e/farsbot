import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import pytz
import threading
import time
import random

from word import daily_words
from gram import grammar_lessons
from tests import daily_tests

TOKEN = "7962643816:AAFIa0wZ4iVKSCoNO9Jfeuv6m33Uf_77SXY"
CHANNEL_USERNAME = "@farsdersler"
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

# ---- FUNKSİYALAR ----
sent_flags = {}  # Gün üzrə hansı göndərilib

def send_daily_content():
    days = list(daily_words.keys())
    current_day_index = 0
    sent_flags.clear()

    while current_day_index < len(days):
        now = datetime.now(pytz.timezone("Asia/Baku"))
        hour, minute = now.hour, now.minute
        day = days[current_day_index]

        if day not in sent_flags:
            sent_flags[day] = {"words": False, "grammar": False, "test": False}

        # ---- SÖZLƏR ----
        if hour == 23 and minute == 17 and not sent_flags[day]["words"]:
            words = daily_words[day]
            text = f"📖 {day} - Günün sözləri:\n"
            for w in words:
                text += f"{w[0]} • {w[1]} • {w[2]}\n"
            bot.send_message(CHANNEL_USERNAME, text=text)
            sent_flags[day]["words"] = True

        # ---- QRAMMATİKA ----
        if hour == 23 and minute == 18 and not sent_flags[day]["grammar"]:
            lesson = grammar_lessons.get(day)
            if lesson:
                text = f"📚 {day} - Gündəlik Qrammatika ({lesson['ders']}):\n{lesson['izah']}\nNümunə: {lesson['nümunə']}"
                bot.send_message(CHANNEL_USERNAME, text=text)
            sent_flags[day]["grammar"] = True

        # ---- TEST ----
        if hour == 23 and minute == 19 and not sent_flags[day]["test"]:
            test = daily_tests.get(day)
            if test:
                for idx, q in enumerate(test['sual'], 1):
                    sual_text, variants, correct_index = q
                    # Variantları qarışdır
                    choices = variants.copy()
                    random.shuffle(choices)

                    kb = InlineKeyboardMarkup()
                    for i, var in enumerate(choices):
                        # Callback data: gün_sualidx_variantidx_düzsəhf
                        is_correct = "1" if var == variants[correct_index] else "0"
                        kb.add(InlineKeyboardButton(var, callback_data=f"{day}_q{idx}_{is_correct}"))

                    bot.send_message(CHANNEL_USERNAME, f"{idx}. {sual_text}", reply_markup=kb)
            sent_flags[day]["test"] = True

        # ---- GÜN SONU 00:00 ----
        if hour == 0 and minute == 0:
            current_day_index += 1

        time.sleep(20)

# ---- CALLBACK HANDLER: INLINE BUTTON ----
@bot.callback_query_handler(func=lambda call: True)
def handle_quiz(call):
    if "_q" in call.data:
        parts = call.data.split("_q")
        day = parts[0]
        q_part = parts[1]
        question_idx, is_correct = q_part.split("_")
        is_correct = bool(int(is_correct))
        if is_correct:
            bot.answer_callback_query(call.id, "✅ Düzgün cavab!")
        else:
            bot.answer_callback_query(call.id, "❌ Səhf cavab!")

# ---- THREAD ----
threading.Thread(target=send_daily_content).start()

# ---- BOT POLLING ----
bot.infinity_polling()
