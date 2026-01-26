import telebot
from datetime import datetime, date
import pytz
import time
import random
import threading
import sqlite3

from word import daily_words
from gram import grammar_lessons
from tests import daily_tests

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8545859230:AAEYjGfFswCEHUYMheZOr9e3hKX0KrJiDik"
CHANNEL_USERNAME = "@farscaaa"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

TZ = pytz.timezone("Asia/Baku")

COURSE_START_DATE = date(2026, 1, 20)

def get_today_day():
    today = datetime.now(TZ).date()
    diff = (today - COURSE_START_DATE).days
    days = list(daily_words.keys())
    if 0 <= diff < len(days):
        return days[diff]
    return None

# ================= DATABASE =================
conn = sqlite3.connect("daily_sent.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sent (
    date TEXT PRIMARY KEY,
    words INTEGER DEFAULT 0,
    grammar INTEGER DEFAULT 0,
    test INTEGER DEFAULT 0
)
""")
conn.commit()

def ensure_today_row():
    today = str(datetime.now(TZ).date())
    cursor.execute("SELECT 1 FROM sent WHERE date=?", (today,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO sent(date) VALUES(?)", (today,))
        conn.commit()

def check_sent(content):
    today = str(datetime.now(TZ).date())
    cursor.execute("SELECT words, grammar, test FROM sent WHERE date=?", (today,))
    row = cursor.fetchone()
    if not row:
        return False
    return row[{"words":0,"grammar":1,"test":2}[content]] == 1

def mark_sent(content):
    today = str(datetime.now(TZ).date())
    cursor.execute(f"UPDATE sent SET {content}=1 WHERE date=?", (today,))
    conn.commit()

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
SEND_HOURS = {
    "words": (11, 15),      # 08:30
    "grammar": (12, 00),   # 13:45
    "test": (19, 00)       # 20:15
}

def daily_sender():
    while True:
        ensure_today_row()
        now = datetime.now(TZ)
        hour, minute = now.hour, now.minute
        day = get_today_day()
        if not day:
            time.sleep(30)
            continue

        # WORDS
        wh, wm = SEND_HOURS["words"]
        if (hour == wh and minute == wm) and not check_sent("words"):
            text = f"📖 {day} – Günün sözləri:\n\n"
            for w in daily_words[day]:
                text += f"• {w[0]} — {w[1]} — {w[2]}\n"
            bot.send_message(CHANNEL_USERNAME, text)
            mark_sent("words")

        # GRAMMAR
        gh, gm = SEND_HOURS["grammar"]
        if (hour == gh and minute == gm) and not check_sent("grammar"):
            lesson = grammar_lessons.get(day)
            if lesson:
                text = (
                    f"📚 {day} – Qrammatika\n\n"
                    f"<b>{lesson['ders']}</b>\n\n"
                    f"{lesson['izah']}\n\n"
                    f"Nümunə:\n{lesson['nümunə']}"
                )
                bot.send_message(CHANNEL_USERNAME, text)
            mark_sent("grammar")

        # TEST
        th, tm = SEND_HOURS["test"]
        if (hour == th and minute == tm) and not check_sent("test"):
            send_tests(day)
            mark_sent("test")

        time.sleep(20)  # hər 20 saniyədən bir yoxlayır

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
            is_anonymous=True
        )
        time.sleep(60)  # poll arası 1 dəqiqə

# ================= ADMIN PANEL =================
@bot.message_handler(commands=['adminpanel'])
def admin_panel(message):
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton("🔄 Təkrar Dərs", callback_data="repeat"),
        InlineKeyboardButton("⭕ Qrammatika", callback_data="only_grammar")
    )
    kb.row(
        InlineKeyboardButton("♂️ Test", callback_data="only_test"),
        InlineKeyboardButton("💬 Söz", callback_data="only_words")
    )
    bot.send_message(
        message.chat.id,
        "Zəhmət olmasa panel qismini seçib davam edin ✅",
        reply_markup=kb
    )

@bot.callback_query_handler(func=lambda c: c.data in ["repeat","only_grammar","only_test","only_words"])
def admin_actions(call):
    day = get_today_day()
    if not day:
        bot.send_message(call.message.chat.id, "Bugün üçün dərs mövcud deyil.")
        return

    if call.data == "repeat":
        choices = []
        # sözlər
        if day in daily_words:
            text = f"📖 {day} – Günün sözləri:\n\n"
            for w in daily_words[day]:
                text += f"• {w[0]} — {w[1]} — {w[2]}\n"
            choices.append(text)
        # qrammatika
        if day in grammar_lessons:
            lesson = grammar_lessons[day]
            text = (
                f"📚 {day} – Qrammatika\n\n"
                f"<b>{lesson['ders']}</b>\n\n"
                f"{lesson['izah']}\n\n"
                f"Nümunə:\n{lesson['nümunə']}"
            )
            choices.append(text)
        # test
        if day in daily_tests:
            tests = daily_tests[day]
            if tests:
                q, options, correct = random.choice(tests)
                shuffled = options.copy()
                random.shuffle(shuffled)
                correct_id = shuffled.index(options[correct])
                bot.send_poll(
                    chat_id=call.message.chat.id,
                    question=q,
                    options=shuffled,
                    type="quiz",
                    correct_option_id=correct_id,
                    is_anonymous=True
                )
                return
        # random seçim
        if choices:
            bot.send_message(call.message.chat.id, random.choice(choices))

    elif call.data == "only_grammar":
        lesson = grammar_lessons.get(day)
        if lesson:
            text = (
                f"📚 {day} – Qrammatika\n\n"
                f"<b>{lesson['ders']}</b>\n\n"
                f"{lesson['izah']}\n\n"
                f"Nümunə:\n{lesson['nümunə']}"
            )
            bot.send_message(call.message.chat.id, text)

    elif call.data == "only_test":
        tests = daily_tests.get(day)
        if tests:
            q, options, correct = random.choice(tests)
            shuffled = options.copy()
            random.shuffle(shuffled)
            correct_id = shuffled.index(options[correct])
            bot.send_poll(
                chat_id=call.message.chat.id,
                question=q,
                options=shuffled,
                type="quiz",
                correct_option_id=correct_id,
                is_anonymous=True
            )

    elif call.data == "only_words":
        if day in daily_words:
            text = f"📖 {day} – Günün sözləri:\n\n"
            for w in daily_words[day]:
                text += f"• {w[0]} — {w[1]} — {w[2]}\n"
            bot.send_message(call.message.chat.id, text)

# ================= START THREAD =================
threading.Thread(target=daily_sender, daemon=True).start()
bot.infinity_polling()
