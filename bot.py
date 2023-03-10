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
async def participant(user_id: int):
    if Channel_Id is None:
        return True
    try:
        await bot.get_chat_member(Channel_Id, user_id)
    except ChatAdminRequired:
        print(f"Please Add the Bot to @{Config.Bot_Channel} as Admin")
        return True
    except UserNotParticipant:
        buttons = [[InlineKeyboardButton('Unete Para Usar El BoT', url=f'https://t.me/{Channel_Id}')]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(user_id, 'Unete', reply_markup=reply_markup)
        return False
    else:
        return True
#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(bot, message):
   # await wait(message.chat.id)
    username = message.from_user.username

    if participant(message.chat.id) == False
        await bot.send_message(username, 'Holka')



bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
