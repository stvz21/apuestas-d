from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from json import loads,dumps

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5871277082:AAFsEc0clhaeJ0wokJVfGF0_P3P0385Sb0M"
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
Channel_Id = -1001807229422
msg_id = 5

#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(bot, message):
    send = message.reply
    username = message.from_user.username  
  #  send_db = bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))
    msg = await bot.get_messages(Channel_Id,message_ids=msg_id) 
    config = loads(msg.text)
    if username in msg.text:
        await send("Hola")
    else:
        config[username] = {"saldo": 0}
        await send("Hi, x 1ra vez")
    await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))

@bot.on_message(filters.command('saldo') & filters.private & filters.incoming)
async def help(bot, message):
    send = message.reply
    username = message.from_user.username
    msg = await bot.get_messages(Channel_Id,message_ids=msg_id)
    config = loads(msg.text)
    saldo = int(config[username]["saldo"])
    new_saldo = saldo - 50
    await send(srt(new_saldo)

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
