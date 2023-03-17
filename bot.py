import asyncio
import time
import requests
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

##callback
inicio = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('💰 Saldo 💰', callback_data="dinero"),
        InlineKeyboardButton('💸 Apostar 💸', callback_data="apost")],
        #InlineKeyboardButton('📈 Info Del BoT 📈', callback_data="infobot")],
        [InlineKeyboardButton('⚠️🆘⛑️ Ayuda ⛑️ 🆘 ⚠️', callback_data="ayuda")
        ]]
    )

atras = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Atas 🔙', callback_data="inicio")
        ]]
    )

adm = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👨🏻‍💻Administrador👨🏻‍💻', url="https://t.me/apuestasDCuba"),
        InlineKeyboardButton('🔙 Atras 🔙', callback_data="inicio")
        ]]
    )
#####
@bot.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    username = msg.from_user.username
    msgs = await bot.get_messages(Channel_Id,message_ids=msg_id)
    if msg.data == "dinero":
        config = loads(msgs.text)
        saldo = str(config[username]["saldo"])
        await msg.message.edit(
             text="**Su Saldo Actual es de:** "+saldo+"** cup**",
             reply_markup=atras
        ) 
    elif msg.data == "inicio":
        await msg.message.edit(
            text="**Hola **"+username+"**\nBienvenido al BoT de Apuestas 🎰 Deportivas de Cuba🇨🇺**",
            reply_markup=inicio
        )
#Comandos
@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(bot, message):
    send = message.reply
    username = message.from_user.username  
  #  send_db = bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))
    msg = await bot.get_messages(Channel_Id,message_ids=msg_id) 
    config = loads(msg.text)
    if username in msg.text:
        await send("**Hola **@"+username+"** Bienvenido al BoT de Apuestas 🎰 Deportivas de Cuba🇨🇺**", reply_markup=inicio)
    else:
        config[username] = {"saldo": 0}
        await send("**Hola **@"+username+"** Bienvenido al BoT de Apuestas 🎰 Deportivas de Cuba🇨🇺**", reply_markup=inicio)
    await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))

@bot.on_message(filters.command('enviar_apuesta') & filters.private & filters.incoming)
async def enviar_apuesta(bot, message):
    send = message.reply
    username = message.from_user.username  
    msgs = await bot.get_messages(Channel_Id,message_ids=msg_id)
    config = loads(msgs.text)
    dinero = float(config[username]["saldo"])
    diner = str(dinero)
    saldo = float(message.text.split("\n")[1])
    deporte = str(message.text.split("\n")[1])
    partido = str(message.text.split("\n")[2])
    apuesta = str(message.text.split("\n")[3])
    sal = str(saldo)
    msg = "**💪🏻👀Datos De su Apuestas 💰💰\n\n**"
    msg += "**🥅Deporte: **"+deporte
    msg += "**⚽Partido: **"+partido+"\n\n"
    msg += "**🪙Apuesta: **"+deporte+"\n\n"
    msg += "**💰Dinero Apostado: **"+sal+"** cup**\n\n"
    if diner <= 0:
        await send("**No tiene saldo en su cuenta para realizar apuetas\nPor Favor Deposite Antes**")
    elif saldo < 25:
        await send("**La Apuesta Mínima es de 25 cup\nSaldo: **"+diner+"** cup**")
    elif diner < saldo:
        await send ("**Está intentando aportar más de su saldo Disponible\nSaldo: **"+diner+"** cup**")
    else:
        restante = float(diner - saldo)
        config[username]["saldo"] = restante
        res = str(restante)
        await send(msg+"\n\nSe Descontó: - "+saldo+" cup\nSaldo Restante: "+res)
       

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


@bot.on_message(filters.command('com') & filters.private & filters.incoming)
async def com(bot, message):
    send = message.reply
    username = message.from_user.username
   # await message.reply("Cuál es Tu edad", reply_markup=ForceReply()) 
    message.text = edad()
 #   await bot.send_message(username, text = "Introduce Tu edad", reply_markup=ForceReply()) 
    await send(message.text)
 
@bot.on_message(filters.command('url') & filters.private & filters.incoming)
async def url(bot, message):
    send = message.reply
    username = message.from_user.username
    url = requests.post('https://eduvirtual.uho.edu.cu/login/index.php')
    urls = str(url)
    await send(urls) 
    
def edad(bot, message):
    bot.send_message(username, text = "Introduce Tu edad", reply_markup=ForceReply()) 
    return


bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.add_handler(MessageHandler(edad))
bot.loop.run_forever()
