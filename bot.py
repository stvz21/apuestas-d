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
        await send("**La Apuesta Mínima es de 25 cup\nSaldo: **"+sal)
    elif saldo < apuesta:
        await send ("**Está intentando aportar más de su saldo Disponible\nSaldo: **+sal")
    else:
        apuest = str(apuesta)
        res = float(saldo - apuesta)
        sald = str(res)
        config[username]["saldo"] = res
        await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))
        await send("Se Descontó: -"+apuest+"\nSaldo Restante: "+saldo)

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
