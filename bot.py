from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import sample, choice
import pytz

import config
import database
from words import WORDS
from gram import GRAMMAR
from tests import TESTS

app = Client(
    "farsbot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

user_state = {}

# ================= START =================
@app.on_message(filters.command("start"))
async def start(_, m: Message):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("📜 Anket", callback_data="anket")]
    ])
    await m.reply(
        "Salam zəhmət olmasa `Anket` buttonuna toxunaraq məlumatları doldurun ✍️",
        reply_markup=kb
    )

# ================= ANKET =================
@app.on_callback_query(filters.regex("anket"))
async def anket(_, q):
    await q.message.delete()
    user_state[q.from_user.id] = "name"
    await q.message.reply("**Adınız Nədir?**")

@app.on_message(filters.private & filters.text)
async def anket_steps(_, m: Message):
    uid = m.from_user.id

    if uid not in user_state:
        await help_answer(m)
        return

    if user_state[uid] == "name":
        database.cur.execute(
            "INSERT OR IGNORE INTO users (user_id,name) VALUES (?,?)",
            (uid, m.text)
        )
        database.db.commit()
        user_state[uid] = "age"
        await m.reply("**Yaşınız neçədir?**")

    elif user_state[uid] == "age":
        if not m.text.isdigit():
            return await m.reply("Yaşı rəqəmlə yazın")
        database.cur.execute(
            "UPDATE users SET age=? WHERE user_id=?",
            (m.text, uid)
        )
        database.db.commit()
        user_state[uid] = "accept"
        await m.reply("**Dərslərə qoşulmaqa könüllü razısınızmı?\nBəli / Xeyr**")

    elif user_state[uid] == "accept":
        if m.text.lower() not in ["bəli", "xeyr"]:
            return await m.reply("Yalnız Bəli və ya Xeyr")
        database.cur.execute(
            "UPDATE users SET accepted=? WHERE user_id=?",
            (m.text, uid)
        )
        database.db.commit()
        del user_state[uid]

        if m.text.lower() == "bəli":
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Dərs Kanalı", url="https://t.me/farsdersleri")]
            ])
            await m.reply(
                "**Zəhmət olmasa** `Dərs Kanalı` **buttonuna toxunaraq kanala qatılın**",
                reply_markup=kb
            )
        else:
            await m.reply(
                "**Könüllü razılığınız olmadığı üçün sizi dərs kanalına qata bilməyəcəm**"
            )

# ================= GÜNÜN SÖZLƏRİ =================
async def send_daily_words():
    words = sample(WORDS, 5)
    text = "\n".join([f"{f} • {a}" for f, a in words])
    await app.send_message(config.CHANNEL_LINK, text)

# ================= QRAMMATİKA =================
async def send_grammar():
    await app.send_message(config.CHANNEL_LINK, choice(GRAMMAR))

# ================= TEST =================
async def send_test():
    t = choice(TESTS)
    await app.send_message(config.CHANNEL_LINK, t["test"])

async def send_answers():
    t = choice(TESTS)
    await app.send_message(config.CHANNEL_LINK, t["answers"])

# ================= ADMIN /gsoz =================
@app.on_message(filters.command("gsoz") & filters.reply & filters.user(config.ADMIN_IDS))
async def admin_word(_, m: Message):
    await app.send_message(config.CHANNEL_LINK, m.reply_to_message.text)

# ================= PM CAVAB =================
async def help_answer(m: Message):
    await m.reply(
        "📘 Bu bot fars dili üçündür.\n"
        "Sözlər, qrammatika və testlərlə bağlı sual verə bilərsiniz."
    )

# ================= SCHEDULER =================
scheduler = AsyncIOScheduler(timezone=pytz.timezone(config.TIMEZONE))
scheduler.add_job(send_daily_words, "cron", hour=20, minute=23)  # Günün sözləri
scheduler.add_job(send_grammar, "cron", hour=13, minute=24)                  # Qrammatika
scheduler.add_job(send_test, "cron", hour=19, minute=25)                     # Test
scheduler.add_job(send_answers, "cron", hour=21, minute=26)                  # Test cavabları
scheduler.start()

app.run()
