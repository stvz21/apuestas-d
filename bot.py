from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5999344767:AAFh7elZ_HiuZ8GLJ3K63LQnV3Nu8RSrndY"
Channel_Id = 'FreeZoneDownloader'
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

USERS = {}
#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(bot, message):
    send = message.reply
    username = message.from_user.username  
    if username in USERS:
        send("Hola")
    else:
        USERS[username] = {saldo: 0}
        await bot.send_message(5416296262, 'El Usuario @{username} Inicio el BoT')
        await bot.send(username, 'Hola, Bienvenido al bot de apuestas 🎰')



bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
