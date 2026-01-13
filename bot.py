import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
import random

from word import daily_words
from gram import grammar_lessons
from tests import daily_tests  # Testlərdə default cavablar da var

TOKEN = "BOT_TOKENİNİZİ_BURAYA_QOYUN"
CHANNEL_ID = "@kanal_username"
ADMIN_ID = 123456789

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
user_data = {}

# Start və Anket
@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📜 Anket", callback_data="anket"))
    bot.send_message(message.chat.id,
                     "Salam zəhmət olmasa Anket buttonuna toxunaraq məlumatları doldurun ✍️",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "anket")
def anket(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    msg = bot.send_message(call.message.chat.id, "Adınız Nədir?")
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    user_data[message.from_user.id] = {"ad": message.text}
    msg = bot.send_message(message.chat.id, "Yaşınız neçədir?")
    bot.register_next_step_handler(msg, get_age)

def get_age(message):
    user_data[message.from_user.id]["yas"] = message.text
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Bəli", callback_data="vol_yes"),
        InlineKeyboardButton("Xeyr", callback_data="vol_no")
    )
    bot.send_message(message.chat.id, "Dərslərə qoşulmaqa könüllü razısınızmı?", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data in ["vol_yes", "vol_no"])
def volunteer(call):
    if call.data == "vol_yes":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📚 Dərs Kanalı", url="https://t.me/kanal_linkiniz"))
        bot.send_message(call.message.chat.id,
                         "Zəhmət olmasa Dərs Kanalı buttonuna toxunaraq kanala qatılın",
                         reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id,
                         "Könüllü razılığınız olmadığı üçün sizi dərs kanalına qata bilməyəcəm")

# Admin manual söz göndərmə
@bot.message_handler(commands=["gsoz"])
def admin_add_word(message):
    if message.from_user.id != ADMIN_ID:
        return
    if message.reply_to_message:
        bot.send_message(CHANNEL_ID, message.reply_to_message.text)

# Günlük ardıcıllıq
current_day_index = 0
days_list = list(daily_words.keys())
tz = pytz.timezone("Asia/Baku")

scheduler = BackgroundScheduler(timezone=tz)

# 08:00 Günün sözləri
def send_daily_words():
    global current_day_index
    today_day = days_list[current_day_index]
    msg = ""
    for w in daily_words[today_day]:
        msg += f"{w[0]} • {w[1]} • {w[2]}\n"
    bot.send_message(CHANNEL_ID, msg)

# 13:00 Qrammatika
def send_daily_grammar():
    bot.send_message(CHANNEL_ID, "Gündəlik Qrammatika:\n\n" + "\n".join(grammar_lessons))

# 19:00 Günün testi (3 söz + 2 qrammatika)
def send_daily_test():
    global current_day_index
    today_day = days_list[current_day_index]
    words = daily_words[today_day]

    # 3 sual sözlərdən (random)
    word_questions = random.sample(words, min(3, len(words)))
    word_sual = [f"Sual • {w[2]} sözünü fars dilində yazın?" for w in word_questions]
    word_cavab = [f"Cavab • {w[0]}" for w in word_questions]

    # 2 sual qrammatikadan (random)
    gram_questions = random.sample(grammar_lessons, 2)
    gram_sual = [f"Sual • {q} haqqında sual" for q in gram_questions]
    gram_cavab = [f"Cavab • Nümunə / izah: {q}" for q in gram_questions]

    # Bir mesajda suallar
    test_msg = "\n".join(word_sual + gram_sual)
    bot.send_message(CHANNEL_ID, "Günün testi:\n\n" + test_msg)

    # Cavablar 21:00
    def send_answers():
        ans_msg = "\n".join(word_cavab + gram_cavab)
        bot.send_message(CHANNEL_ID, "Günün test cavabları:\n\n" + ans_msg)
        # Növbəti günə keç
        global current_day_index
        current_day_index += 1
        if current_day_index >= len(days_list):
            current_day_index = 0

    scheduler.add_job(send_answers, 'cron', hour=21, minute=0)

# Scheduler əlavə et
scheduler.add_job(send_daily_words, 'cron', hour=8, minute=0)
scheduler.add_job(send_daily_grammar, 'cron', hour=13, minute=0)
scheduler.add_job(send_daily_test, 'cron', hour=19, minute=0)

scheduler.start()
bot.infinity_polling()
