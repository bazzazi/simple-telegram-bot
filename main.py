import api as C
import Responses as R
from telegram.ext import *

print("bot started....")
def main():
    updater=Updater(C.API_BOT, use_context=1)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",Help))
    dp.add_handler(MessageHandler(Filters.text,handle_response))

    updater.start_polling()
    updater.idle()

def start(update, context):
    update.message.reply_text("ربات اجرا شد")
def Help(update, context):
    update.message.reply_text("حرف بزنید")

def handle_response(update, context):
    text=update.message.text
    update.message.reply_text(R.Responses(str(text)))

main()