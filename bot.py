from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = os.environ.get('bot_token')
Channel_Id = 'FreeZoneDownloader'
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

#Acceso
def participant(msg.chat.id):
    if Channel_Id is None:
        return True
    try:
        await bot.get_chat_member(Channel_Id, user_id)
    except ChatAdminRequired:
       # print(f"Please Add the Bot to @{Config.Bot_Channel} as Admin")
        return True
    except UserNotParticipant:
        buttons = [[InlineKeyboardButton('het', url=f'https://t.me/{Channel_Id}')]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(user_id, 'hii', reply_markup=reply_markup)
        return False
    else:
        return True
#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(_, msg: Message):
   # await wait(msg.chat.id)
    username = msg.from_user.username
    await bot.send_message(username, '11a')
    if not await participant(msg.chat.id):
        return
    await bot.send_message(username, 'Holka')



bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
