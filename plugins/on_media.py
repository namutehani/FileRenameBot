from pyrogram import Client
from pyrogram.types import Message
from bot import Bot

@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.channel & ~filters.edited)
async def on_media_handler(c: Client, m: Message):
    name = m.document.file_name
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await asyncio.sleep(3)
    await m.reply_text(name,quote=True)
