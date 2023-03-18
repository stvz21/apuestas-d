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
bot_token = "5871277082:AAFsEc0clhaeJ0wokJVfGF0_P3P0385Sb0M"
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
Channel_Id = -1001807229422
msg_id = 5

##callback 
enviar = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📤💰 Enviar Apuesta 💰📤', callback_data="enviar_a")],
        [InlineKeyboardButton('⛔ Cancelar ⛔', callback_data="cancel")
    #    InlineKeyboardButton('📈 Info Del BoT 📈', callback_data="infobot"),
     #   [InlineKeyboardButton('⚠️🆘⛑️ Ayuda ⛑️ 🆘 ⚠️', callback_data="ayuda")
        ]]
    )
inicio = InlineKeyboardMarkup(
        [[ 
        InlineKeyboardButton('💸 Apostar 💸', callback_data="apost")],
        [InlineKeyboardButton('💰 Balance 💰', callback_data="dinero"),
        InlineKeyboardButton('📤💰 Retirar 💰📤', callback_data="retirar")],
        [InlineKeyboardButton('📥💰 Depositar 💰📥', callback_data="depositar")],
       # [InlineKeyboardButton('⚠️🆘⛑️ Ayuda ⛑️ 🆘 ⚠️', callback_data="ayuda")],
        [InlineKeyboardButton('🗯️Canal🔖', url="https://luis.com"),
        InlineKeyboardButton('💭Chat🗨️', url="https://Luis.com")
        ]]
    )

atras = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Atas 🔙', callback_data="inicio")
        ]]
    )

adm = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👨🏻‍💻Administrador👨🏻‍💻', url="https://t.me/apuestasDCuba")],
        [InlineKeyboardButton('🔙 Atras 🔙', callback_data="inicio")
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
    elif msg.data == "enviar_a":       
        config = loads(msgs.text)
        res = float(config[username]["saldo"]) - float(config[username]["apostando"])
        resul = str(res)
        await msg.message.edit(
            text="**Apuesta Enviada Correctamente✅✅\nSaldo Restante: **"+resul+"** cup\n\n**"+msg.message.text
         #   reply_markup=inicio
        )
        await bot.send_message(Channel_Id, msg.message.text)
        config[username]["apostando"] = 0
        config[username]["saldo"] = res
        await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))

    elif msg.data == "cancel":
        await msg.message.delete()
        config = loads(msgs.text)
        config[username]["apostando"] = 0
        await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(config,indent=4))
      #  await msg.message.edit(
       #     text="**Apuesta Enviada Correctamente\n\n**"+msg.message.text
         #   reply_markup=inicio
       # )

    elif msg.data == "depositar":
        await msg.message.edit(
            text="**Para depositar debes de realizar la tranferencia a los datos, y luego contactar con el Administrador y enviar captura de pantalla de la tranferencia, luego de verificar, recargue su cuenta en el BoT\n\nPreguntas Frecuentes:\n\nMetodos de Depósito:\nPuede ser:\nSaldo:** `51405424`**\nTarjeta:** `7374 3833 8393 3933`\n\n**¿Cuál es el Depósito mínimo?\nEl depósito mínimo es de 25 cup\nSi el depósito es mediante saldo se le descontará un 10% del monto depositado. Ejemplo: Si Deposita 100 cup se le recargará 90 cup válidos para q realice apuestas 🎰**",
            reply_markup=adm
        )

    elif msg.data == "retirar":
        await msg.message.edit(
            text="**Para Retirar 💰 Contacta con el Administrador\n\nPara realizar debe ser un monto mayor a 25 cup y solo se puede realizar 1 retiro cada 2 Días**",
            reply_markup=adm
        )

    elif msg.data == "apost":
        await bot.send_photo(username,"logo.jpg",caption="**Para apostar debe hacerlo de la siguiente manera:\nDebe Unirse al Canal donde se enviaran los partidos disponibles para realizar apuestas, luego para realizar la apuesta llena sus datos de la siguiente forma:\n\n/enviar_apuesta\nCantidad que va a apostar\nPartido\nApuesta\n\nEjemplo:\n\n/enviar_apuesta\n50\nReal Madrid vs Barcelona\nGana Real Madrid**")

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
    deporte = str(message.text.split("\n")[2])
    partido = str(message.text.split("\n")[3])
    apuesta = str(message.text.split("\n")[4])
    sal = str(saldo)
    msg = "**💪🏻👀Datos De su Apuestas 💰💰\n\n**"
    msg += "**👤Usuario: **"+username+"\n\n"
    msg += "**🥅Deporte: **"+deporte+"\n\n"
    msg += "**⚽Partido: **"+partido+"\n\n"
    msg += "**🏆Apuesta: **"+apuesta+"\n\n"
    msg += "**💰Dinero Apostado: **"+sal+"** cup**\n\n"
    if dinero <= 0:
        await send("**No tiene saldo en su cuenta para realizar apuetas\nPor Favor Deposite Antes**")
    elif saldo < 25:
        await send("**La Apuesta Mínima es de 25 cup\nSaldo: **"+diner+"** cup**")
    elif dinero < saldo:
        await send ("**Está intentando aportar más de su saldo Disponible\nSaldo: **"+diner+"** cup**")
    else:
        restante = float(dinero - saldo)
        config[username]["apostando"] = saldo
        res = str(restante)
        await send(msg, reply_markup=enviar)
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
