import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import *
#NAME -> YOUR BOTS FILE NAME 
from AnonXMusic import app


@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"𝘾𝙊𝙎𝙋𝙇𝘼𝙔 𝘽𝙔 𝙍𝙄𝘼𝙎")

@app.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("𝙊𝙉𝙇𝙔 𝙒𝙊𝙍𝙆 𝙄𝙉 𝘿𝙈",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ",url=f"https://t.me/{app.me.username}?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()

       await msg.reply_photo(ncosplay, caption=f"𝘾𝙊𝙎𝙋𝙇𝘼𝙔 𝘽𝙔 𝙍𝙄𝘼𝙎")


__mod_name__ = "ᴄᴏsᴘʟᴀʏ"
__help__ = """
 ❍ /cosplay ➛ ʀᴀɴᴅᴏᴍ ᴄᴏsᴘʟᴀʏ ɪᴍᴀɢᴇ.
 
 ❍ /ncosplay ➛ ʀᴀɴᴅᴏᴍ ɴᴜᴅᴇ ᴄᴏsᴘʟᴀʏ ɪᴍᴀɢᴇ.
 """
 
