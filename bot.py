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
msg_id 5

#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(bot, message):
    send = message.reply
    username = message.from_user.username  
    send_db = bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))
    msg = await bot.get_messages(Channel_Id,message_ids=msg_id) 
    config = loads(msg.text)
    if username in msg.text:
        await send("Hola")
    else:
        config[username] = {"saldo": 0}
        await send("Hi, x 1ra vez")
    await send_db

@bot.on_message(filters.command('help') & filters.private & filters.incoming)
async def help(bot, message):
    send = message.reply
    username = message.from_user.username
    base = str(USERS)
    await bot.send_message(5416296262, base)

def update(username):
    USERS[username] = {"saldo": 0}

async def get_messages():
    msg = await bot.get_messages(-1001807229422,message_ids=5)
    USERS.update(loads(msg.text))
    await bot.send_message(5416296262, "Cargo el user")
async def send_config():
    try:
        await bot.edit_message_text(-1001807229422,message_id=5,text=dumps(config,indent=4))
    except:	
        pass

bot.on_message(filters.command('db') & filters.private & filters.incoming)
async def db(bot, message):
    send = message.reply
    username = message.from_user.username
   # await send("Mensaje 1")
    get_messages()


bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
