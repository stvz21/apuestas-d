from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from json import loads,dumps

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
    
    #USERS[username] = {'saldo': 0}
    await bot.send_message(5416296262, 'El Usuario @'+username+' Inicio el BoT')
   # await bot.send_message(5416296262, base)
    await send('Hola, Bienvenido al bot de apuestas 🎰')
 #   await bot.edit_message_text(-1001807229422,message_id=5,text="Hola, Viste edite el mensaje")
    msg = await bot.get_messages(-1001807229422,message_ids=5)
  #  Configs.update(loads(msg.text))
    await send(msg.text)
 #   await bot.send_message(5416296262, USERS)
   # await bot.edit_message_text(-1001807229422,message_id=5,text="Hola, Viste edite el mensaje")
    db = msg.text
    USERS = str(db)
   # await bot.send_message(5416296262, USERS)
 #   try:await get_messages()
   # await send_config()
 #   base = str(USERS)
    await send(db)
    get_messages()
@bot.on_message(filters.command('jj') & filters.private & filters.incoming)
async def jj(bot, message):
    send = message.reply
    username = message.from_user.username
    base = str(USERS)
    await bot.send_message(5416296262, base)
###
@bot.on_message(filters.command('sen') & filters.private & filters.incoming)
async def sen(bot, message):
    send = message.reply
    username = message.from_user.username
    msg = await bot.get_messages(-1001807229422,message_ids=5) 
    conf = loads(msg.text)
    if username in msg.text:
        conf[username]["saldo"] = 10
        await send("Tienes Acceso")
        await send(conf)
    else:
        await send("No Tienes Acceso")

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
        await bot.edit_message_text(-1001807229422,message_id=5,text=dumps(USERS,indent=4))
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
