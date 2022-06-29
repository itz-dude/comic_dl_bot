from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup


def comicindex(client, callback_query):
    dtInitial = callback_query.data
    dtInitialSplit = dtInitial.split("_")
    data = dtInitialSplit[1]
    comiclink = f"https://www.comicextra.com/comic/{data}"
    response = requests.get(comiclink)
    plainText = response.text
    source_url = BeautifulSoup(plainText, "html.parser")
    title = source_url.find('span', attrs={'class': 'title-1'}).text
    chapters_div = source_url.find('tbody', attrs={'id': 'list'})
    chapters = chapters_div.find_all('tr')
    lastChapList = []
    keyb = []
    number = 1
    for links in chapters:        
        chapterNo = number
        lastChapList.append(chapterNo)
        number = number + 1
    lastChapterNo = len(lastChapList)
    if int(lastChapterNo) > 120:
        listInitial = []
        for i in range(0, int(lastChapterNo)):
            listInitial.append(i)
        n = 41
        listOrganisedInitial = [listInitial[i:i + n] for i in range(0, len(listInitial), n)]
        listIndex = []
        for item in listOrganisedInitial:
            listIndex.append((InlineKeyboardButton(f"Ch {item[0]}-{item.pop()}", callback_data=f"but2_{listOrganisedInitial.index(item)}_{data}")))
        o = 3
        listIndexFinal = [listIndex[i:i + o] for i in range(0, len(listIndex), o)]
        repl = InlineKeyboardMarkup(listIndexFinal)
        callback_query.edit_message_text(f"""You selected **{title}**

Select the Chapter""", reply_markup=repl, parse_mode="markdown")
    elif int(lastChapterNo) < 120:
        for i in range(0, int(lastChapterNo)):
            keyb.append((InlineKeyboardButton(f"Ch {i}", callback_data=f"pdfr_{data}_{i}")))
        o = 5
        listIndexFinal = [keyb[i:i + o] for i in range(0, len(keyb), o)]
        repl = InlineKeyboardMarkup(listIndexFinal)
        callback_query.edit_message_text(f"""You selected **{title}**
        
Select the Chapter""", reply_markup=repl, parse_mode="markdown")
