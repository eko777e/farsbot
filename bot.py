import telebot
from datetime import datetime, date
import pytz
import time
import random

from word import daily_words
from gram import grammar_lessons
from tests import daily_tests

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8545859230:AAEYjGfFswCEHUYMheZOr9e3hKX0KrJiDik"
CHANNEL_USERNAME = "@farscaaa"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

TZ = pytz.timezone("Asia/Baku")

# ================= START DATE =================
COURSE_START_DATE = date(2026, 1, 1)  # kursun başladığı gün

# ================= DAY CALCULATOR =================
def get_today_day():
    today = datetime.now(TZ).date()
    diff = (today - COURSE_START_DATE).days
    days = list(daily_words.keys())
    if 0 <= diff < len(days):
        return days[diff]
    return None

# ================= START / ANKET =================
@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📜 Anket", callback_data="anket"))
    bot.send_message(
        message.chat.id,
        "Salam 😊 Zəhmət olmasa Anket buttonuna toxunaraq məlumatları doldurun ✍️",
        reply_markup=kb
    )

@bot.callback_query_handler(func=lambda c: c.data == "anket")
def anket(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    msg = bot.send_message(call.message.chat.id, "Adınız nədir?")
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    msg = bot.send_message(message.chat.id, "Yaşınız neçədir?")
    bot.register_next_step_handler(msg, get_age)

def get_age(message):
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton("Bəli", callback_data="yes"),
        InlineKeyboardButton("Xeyr", callback_data="no")
    )
    bot.send_message(
        message.chat.id,
        "Dərslərə qoşulmağa könüllü razısınızmı?",
        reply_markup=kb
    )

@bot.callback_query_handler(func=lambda c: c.data in ["yes", "no"])
def consent(call):
    if call.data == "yes":
        kb = InlineKeyboardMarkup()
        kb.add(
            InlineKeyboardButton(
                "📚 Dərs Kanalı",
                url=f"https://t.me/{CHANNEL_USERNAME.strip('@')}"
            )
        )
        bot.send_message(call.message.chat.id, "Kanala qoşulun 👇", reply_markup=kb)
    else:
        bot.send_message(call.message.chat.id, "Razılıq olmadığı üçün proses dayandırıldı.")

# ================= DAILY CONTENT =================
sent = {"words": False, "grammar": False, "test": False}

def daily_sender():
    global sent
    while True:
        now = datetime.now(TZ)
        hour, minute = now.hour, now.minute
        day = get_today_day()

        if not day:
            time.sleep(60)
            continue

        # ---- WORDS 08:00 ----
        if hour == 8 and minute == 0 and not sent["words"]:
            text = f"📖 {day} – Günün sözləri:\n\n"
            for w in daily_words[day]:
                text += f"• {w[0]} — {w[1]} — {w[2]}\n"
            bot.send_message(CHANNEL_USERNAME, text)
            sent["words"] = True

        # ---- GRAMMAR 13:00 ----
        if hour == 13 and minute == 0 and not sent["grammar"]:
            lesson = grammar_lessons.get(day)
            if lesson:
                text = (
                    f"📚 {day} – Qrammatika\n\n"
                    f"<b>{lesson['ders']}</b>\n\n"
                    f"{lesson['izah']}\n\n"
                    f"Nümunə:\n{lesson['nümunə']}"
                )
                bot.send_message(CHANNEL_USERNAME, text)
            sent["grammar"] = True

        # ---- TEST 20:00 ----
        if hour == 20 and minute == 0 and not sent["test"]:
            send_tests(day)
            sent["test"] = True

        # ---- RESET AT 00:00 ----
        if hour == 0 and minute == 0:
            sent = {"words": False, "grammar": False, "test": False}

        time.sleep(20)

# ================= TEST SENDER =================
def send_tests(day):
    tests = daily_tests.get(day)
    if not tests:
        return

    for i, (q, options, correct) in enumerate(tests[:5]):
        shuffled = options.copy()
        random.shuffle(shuffled)
        correct_id = shuffled.index(options[correct])

        bot.send_poll(
            chat_id=CHANNEL_USERNAME,
            question=f"{i+1}. {q}",
            options=shuffled,
            type="quiz",
            correct_option_id=correct_id,
            is_anonymous=False
        )
        time.sleep(60)

# ================= START THREAD =================
import threading
threading.Thread(target=daily_sender, daemon=True).start()

bot.infinity_polling()
