import os
from pyrogram import Client, filters


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

bughunter0 = Client(
    "Mp4-to-Mp3-Conveter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")


@bughunter0.on_message(filters.private & filters.text)
async def start(bot, message):
    await message.reply_text("ʜɪ [👋](https://telegra.ph/file/57873ee2279555866f4c9.jpg) ....\nɪ ᴀᴍ ᴍᴘ4 ᴛᴏ ᴍᴘ3 ᴄᴏɴᴠᴇᴛᴇʀ ʙᴏᴛ🤖\nSᴇɴᴅ ᴀ ᴠɪᴅᴇᴏ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ɪɴᴛᴏ ᴀᴜᴅɪᴏ🎷\n\n ʙʏ @TamilBots 😎\n\nᴅᴇᴠ @AboutMk 👻 ")


@bughunter0.on_message(filters.video & filters.private)
async def mp3(bot, message):
    
    # download video
    file_path = DOWNLOAD_LOCATION + f"{message.from_user.id}.mp3"
    txt = await message.reply_text("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ sᴇʀᴠᴇʀ.....")
    await message.download(file_path)
    await txt.edit_text("ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ sᴜᴄᴇᴇssғᴜʟʟʏ")
    
    # convert to audio
    await txt.edit_text("ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴛᴏ ᴀᴜᴅɪᴏ")
    await message.reply_audio(audio=file_path, caption="@TamilBots 👻", quote=True)
    
    # remove file
    try:
        os.remove(file_path)
    except:
        pass
    
    await txt.delete()


bughunter0.run()
