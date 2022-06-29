from pyrogram import *
from pyrogram.types import *

def start(client, message):
    message.reply_text("""**/comic <comic name> to search**
""", parse_mode="markdown")
