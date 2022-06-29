
from pyrogram import *
from pyrogram.filters import regex, text_filter
from pyrogram.methods.utilities.start import Start
import config
import logging
from pyrogram.handlers import *
from plugin.comic_search import comicsearch
from plugin.comic_index import comicindex
from plugin.comic_index2 import comicindex2
from plugin.comic_to_pdf import comic2Pdf
from plugin.start import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


bot = Client(
    "comic",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)



def main():
    bot.add_handler(MessageHandler(comicsearch, filters.regex(r'comic')), group=1)
    bot.add_handler(CallbackQueryHandler(comicindex, filters.regex('but_*')), group=2)
    bot.add_handler(CallbackQueryHandler(comicindex2, filters.regex('but2_*')), group=3)
    bot.add_handler(CallbackQueryHandler(comic2Pdf, filters.regex('pdfr_*')), group=6)
    bot.add_handler(MessageHandler(start , filters.regex(r'start')), group=13)


if __name__ == '__main__':
    bot.run(main())
