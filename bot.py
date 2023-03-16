import asyncio
import time
import request
from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from json import loads,dumps
from pyrogram.types import ForceReply
from pyrogram.handlers import MessageHandler

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5999344767:AAFh7elZ_HiuZ8GLJ3K63LQnV3Nu8RSrndY"
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
        await send("**Hola**@"+username+"** Bienvenido al BoT de Apuestas 🎰**")
    else:
        config[username] = {"saldo": 0}
        await send("**Hola**@"+username+"** Bienvenido al BoT de Apuestas 🎰**")
    await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))

@bot.on_message(filters.command('saldo') & filters.private & filters.incoming)
async def saldo(bot, message):
    send = message.reply
    username = message.from_user.username
    msg = await bot.get_messages(Channel_Id,message_ids=msg_id)
    config = loads(msg.text)
    saldo = float(config[username]["saldo"])
    sal = str(saldo)
    apuesta = float(message.text.split(" ")[1])
    if saldo <= 0:
        await send("**No tiene saldo en su cuenta para realizar apuetas\nPor Favor Deposite Antes**")
    elif apuesta < 25:
        await send("**La Apuesta Mínima es de 25 cup\nSaldo: **"+sal+"cup")
    elif saldo < apuesta:
        await send ("**Está intentando aportar más de su saldo Disponible\nSaldo: **"+sal+" cup")
    else:
        apuest = str(apuesta)
        res = float(saldo - apuesta)
        ssl = str(res)
        config[username]["saldo"] = res
        await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))
        await send("Se Descontó: -"+apuest+"\nSaldo Restante: "+ssl)


@bot.on_message(filters.command('url') & filters.private & filters.incoming)
async def edad(bot, message):
    send = message.reply
    username = message.from_user.username
   # await message.reply("Cuál es Tu edad", reply_markup=ForceReply()) 
    a = message.text
    await bot.send_message(username, text = "Introduce Tu edad", reply_markup=ForceReply()) 
    if message.text != */edad"
         b = message.text  
 
@bot.on_message(filters.command('edad') & filters.private & filters.incoming)
async def edad(bot, message):
    send = message.reply
    username = message.from_user.username
    url = requests.get('https://w3schools.com/python/demopage.htm')
    await send(url)     
    
bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.add_handler(MessageHandler(edad))
bot.loop.run_forever()
