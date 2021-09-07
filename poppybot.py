import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = '1975060818:AAGAnT6Q2JLOQFKCZGjJsT25-EHEa577UVw'
updater = Updater(token= TOKEN, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def roll(update, contex):
    numero = random.randint(1, 12)
    contex.bot.send_message(chat_id = update.effective_chat.id, text = str(numero))

echoMsg = MessageHandler(Filters.text & (~Filters.command), echo)
start_handler = CommandHandler('start', start)
roll_handler = CommandHandler('roll',roll)

dispatcher.add_handler(echoMsg)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(roll_handler)

updater.start_polling()
updater.idle()