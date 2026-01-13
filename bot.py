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

# ================= GÜNÜN KONTENTİNİN YADDA SAXLANMASI =================
daily_data = {
    "words": [],
    "grammar": ""
}

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

# ================= DƏRS KANALINA QATILMA =================
@app.on_chat_member_updated(filters.chat(config.CHANNEL_LINK))
async def new_member(_, event):
    if event.new_chat_member.status == enums.ChatMemberStatus.MEMBER:
        user = event.new_chat_member.user
        await app.send_message(
            config.CHANNEL_LINK,
            f"🗣️ {user.mention(style='md')} **Dərslərimizə qatıldı!!**\n"
            "**Hər kəsə dərslərində uğurlar** 🥳"
        )

# ================= GÜNÜN SÖZLƏRİ =================
async def send_daily_words():
    words = sample(WORDS, 5)
    daily_data["words"] = words  # yadda saxla
    text = "\n".join([f"{f} • {a}" for f, a in words])
    await app.send_message(config.CHANNEL_LINK, f"**Günün sözləri:**\n{text}")

# ================= QRAMMATİKA =================
async def send_grammar():
    grammar = choice(GRAMMAR)
    daily_data["grammar"] = grammar  # yadda saxla
    await app.send_message(config.CHANNEL_LINK, f"**Gündəlik Qrammatika:**\n{grammar}")

# ================= TEST =================
async def send_test():
    if not daily_data["words"] or not daily_data["grammar"]:
        await app.send_message(config.CHANNEL_LINK, "⚠️ Bu günün sözləri və ya qrammatikası yoxdur.")
        return

    t = choice(TESTS)
    # Testi sözlər və qrammatika üzrə düzəldə bilərsən
    test_text = "**Gün sonunun testi!**\n"
    for i, q in enumerate(daily_data["words"] + [daily_data["grammar"]], 1):
        test_text += f"Sual {i} • {q[0] if isinstance(q, tuple) else q}\n"
    daily_data["current_test"] = test_text
    await app.send_message(config.CHANNEL_LINK, test_text)

async def send_answers():
    if "current_test" not in daily_data:
        await app.send_message(config.CHANNEL_LINK, "⚠️ Bu gün üçün test yoxdur.")
        return
    answers_text = "**Gün sonunun test cavabları**\n"
    for i, q in enumerate(daily_data["words"] + [daily_data["grammar"]], 1):
        answers_text += f"Cavab {i} • {q[1] if isinstance(q, tuple) else 'Qrammatika cavabı'}\n"
    await app.send_message(config.CHANNEL_LINK, answers_text)

# ================= ADMIN /gsoz =================
@app.on_message(filters.command("gsoz") & filters.reply & filters.user(config.ADMIN_IDS))
async def admin_word(_, m: Message):
    await app.send_message(config.CHANNEL_LINK, m.reply_to_message.text)

# ================= AI KOMANDA =================
@app.on_message(filters.private & filters.regex(r"^[!/.]sual(?:\s+(.+))?$"))
async def ai_command(_, m: Message):
    user_input = m.matches[0].group(1) if m.matches else ""
    user_input = user_input.strip()
    if not user_input:
        return await m.reply(
            "✍️ Zəhmət olmasa /sual əmri ilə sualınızı yazın.\n"
            "Məsələn: `/sual Fars dili nə üçün önəmlidir?`"
        )
    try:
        resp = requests.post(
            API_URL,
            headers=HEADERS,
            json={
                "message": [{"type": "text", "text": user_input}],
                "chatId": str(m.chat.id),
                "generatorType": "CodeGenerator"
            },
            timeout=10
        )
        if resp.status_code == 200:
            data = resp.json()
            reply_text = data.get("response", "⚠️ Cavab tapılmadı.")
        else:
            reply_text = f"⚠️ Server xətası: {resp.status_code}"
    except Exception as e:
        reply_text = f"❌ Sorğu zamanı xəta baş verdi:\n{e}"
    await m.reply(reply_text)

# ================= SCHEDULER =================
scheduler = AsyncIOScheduler(timezone=pytz.timezone(config.TIMEZONE))
scheduler.add_job(send_daily_words, "cron", hour=21, minute=4)  # Günün sözləri
scheduler.add_job(send_grammar, "cron", hour=21, minute=5)       # Qrammatika
scheduler.add_job(send_test, "cron", hour=21, minute=6)          # Test
scheduler.add_job(send_answers, "cron", hour=21, minute=7)       # Test cavabları
scheduler.start()

app.run()
