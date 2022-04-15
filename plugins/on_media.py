from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
import asyncio

@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.channel & ~filters.edited)
async def on_media_handler(c: Client, m: Message):
    name = m.document.file_name
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await m.reply_text(f"'{name}'",quote=True)
