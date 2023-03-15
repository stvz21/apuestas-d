from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from json import loads,dumps

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5871277082:AAFsEc0clhaeJ0wokJVfGF0_P3P0385Sb0M"
Channel_Id = 'FreeZoneDownloader'
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

USERS = {}
#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(bot, message):
    send = message.reply
    username = message.from_user.username  
    USERS[username] = {'saldo': 0}
    await bot.send_message(5416296262, 'El Usuario @'+username+' Inicio el BoT')
    await bot.send_message(5416296262, USERS)
    await send('Hola, Bienvenido al bot de apuestas 🎰')
 #   await bot.edit_message_text(-1001807229422,message_id=5,text="Hola, Viste edite el mensaje")
    msg = await bot.get_messages(-1001807229422,message_ids=5)
  #  Configs.update(loads(msg.text))
    await send(msg.text)
    USERS.update(loads(msg.text))
 #   await bot.send_message(5416296262, USERS)
   # await bot.edit_message_text(-1001807229422,message_id=5,text="Hola, Viste edite el mensaje")
    await bot.send_message(5416296262, USERS)
bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
