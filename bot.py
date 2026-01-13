from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import sample, choice
import pytz
import requests, json

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

API_URL = "https://aicodegenerator.ifscswiftcodeapp.in/api.php"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

daily_data = {
    "words": [],
    "grammar": []
}

# ================= START =================
@app.on_message(filters.command("start"))
async def start(_, m: Message):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("📜 Anket", callback_data="anket")]
    ])
    await m.reply(
        "Salam 👋\nZəhmət olmasa **Anket** buttonuna toxunaraq məlumatları doldurun ✍️",
        reply_markup=kb
    )

# ================= ANKET =================
@app.on_callback_query(filters.regex("^anket$"))
async def anket(_, q):
    user_state[q.from_user.id] = "name"
    await q.message.edit("**Adınız nədir?**")

@app.on_message(filters.private & filters.text & ~filters.command(["start", "sual"]))
async def anket_steps(_, m: Message):
    uid = m.from_user.id
    if uid not in user_state:
        return

    if user_state[uid] == "name":
        database.cur.execute(
            "INSERT OR IGNORE INTO users (user_id, name) VALUES (?,?)",
            (uid, m.text)
        )
        database.db.commit()
        user_state[uid] = "age"
        await m.reply("**Yaşınız neçədir?**")

    elif user_state[uid] == "age":
        if not m.text.isdigit():
            return await m.reply("Yaşı yalnız rəqəmlə yazın.")
        database.cur.execute(
            "UPDATE users SET age=? WHERE user_id=?",
            (m.text, uid)
        )
        database.db.commit()
        user_state[uid] = "accept"
        await m.reply("**Dərslərə qatılmağa razısınız? (Bəli / Xeyr)**")

    elif user_state[uid] == "accept":
        if m.text.lower() not in ["bəli", "xeyr"]:
            return await m.reply("Yalnız **Bəli** və ya **Xeyr** yazın.")
        database.cur.execute(
            "UPDATE users SET accepted=? WHERE user_id=?",
            (m.text.lower(), uid)
        )
        database.db.commit()
        del user_state[uid]

        if m.text.lower() == "bəli":
            await m.reply(
                "🎉 Əla!\nDərslər kanalında görüşərik:\n"
                "👉 https://t.me/farsdersleri"
            )
        else:
            await m.reply("Razı olmadığınız üçün proses dayandırıldı.")

# ================= GÜNÜN SÖZLƏRİ =================
async def send_daily_words():
    words = sample(WORDS, 5)
    daily_data["words"] = words
    text = "\n".join([f"🔹 {f} — {a}" for f, a in words])
    await app.send_message(config.CHANNEL_ID, f"📘 **Günün sözləri**\n\n{text}")

# ================= QRAMMATİKA =================
async def send_grammar():
    grammar = choice(GRAMMAR)
    daily_data["grammar"] = grammar
    await app.send_message(config.CHANNEL_ID, f"📗 **Günün qrammatikası**\n\n{grammar}")

# ================= TEST =================
async def send_test():
    text = "📝 **Günün testi**\n\n"
    i = 1
    for f, _ in daily_data["words"]:
        text += f"{i}) `{f}` nə deməkdir?\n"
        i += 1
    text += f"\n{i}) Bu günkü qrammatikanı izah edin."
    await app.send_message(config.CHANNEL_ID, text)

# ================= CAVABLAR =================
async def send_answers():
    text = "✅ **Test cavabları**\n\n"
    i = 1
    for _, a in daily_data["words"]:
        text += f"{i}) {a}\n"
        i += 1
    text += f"\n{i}) Qrammatika izah mətni."
    await app.send_message(config.CHANNEL_ID, text)

# ================= AI /sual =================
@app.on_message(filters.command("sual"))
async def ai_command(_, m: Message):
    if len(m.command) < 2:
        return await m.reply(
            "✍️ Sualı belə yazın:\n"
            "`/sual fars dili nə üçün vacibdir?`"
        )

    user_input = " ".join(m.command[1:])

    try:
        resp = requests.post(
            API_URL,
            headers=HEADERS,
            json={
                "message": [{"type": "text", "text": user_input}],
                "chatId": str(m.chat.id),
                "generatorType": "CodeGenerator"
            },
            timeout=15
        )

        if resp.status_code == 200:
            reply_text = resp.json().get("response", "⚠️ Cavab tapılmadı.")
        else:
            reply_text = f"⚠️ Server xətası: {resp.status_code}"

    except Exception as e:
        reply_text = f"❌ Xəta:\n`{e}`"

    await m.reply(reply_text)

# ================= SCHEDULER =================
scheduler = AsyncIOScheduler(timezone=pytz.timezone(config.TIMEZONE))
scheduler.add_job(send_daily_words, "cron", hour=21, minute=4)
scheduler.add_job(send_grammar, "cron", hour=21, minute=5)
scheduler.add_job(send_test, "cron", hour=21, minute=6)
scheduler.add_job(send_answers, "cron", hour=21, minute=7)
scheduler.start()

app.run()
