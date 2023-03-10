from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os


api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = os.environ.get('bot_token')
Channel_Id = -1001804018431
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)




bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
