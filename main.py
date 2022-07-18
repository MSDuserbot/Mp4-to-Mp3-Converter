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
    await message.reply_text("ʜɪ....ɪ ᴀᴍ ᴍᴘ4 ᴛᴏ ᴍᴘ3 ᴄᴏɴᴠᴇᴛᴇʀ ʙᴏᴛ\nSᴇɴᴅ ᴀ ᴠɪᴅᴇᴏ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ɪɴᴛᴏ ᴀᴜᴅɪᴏ\n ʙʏ @TamilBots\nᴅᴇᴠ @AboutMk  ")


@bughunter0.on_message(filters.video & filters.private)
async def mp3(bot, message):
    
    # download video
    file_path = DOWNLOAD_LOCATION + f"{message.from_user.id}.mp3"
    txt = await message.reply_text("Downloading to My server.....")
    await message.download(file_path)
    await txt.edit_text("Downloaded Successfully")
    
    # convert to audio
    await txt.edit_text("Converting to audio")
    await message.reply_audio(audio=file_path, caption="@BugHunterBots", quote=True)
    
    # remove file
    try:
        os.remove(file_path)
    except:
        pass
    
    await txt.delete()


bughunter0.run()
