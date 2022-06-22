import logging
from telegram import Update
from telegram.ext import (ApplicationBuilder, CallbackContext,CommandHandler,
                          ConversationHandler, filters, MessageHandler, ContextTypes)


# user = input("ingresa id de usuario: ")

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

#async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
 #   await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, te buscan en la reja!")
def action (msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text(f"Hola {update.effective_user.first_name}")
    await context.bot.send_message(chat_id=1882099390, text="Te buscan en la reja!")

async def start2(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text(f"Hola {update.effective_user.first_name}")
    await context.bot.send_message(chat_id=1540493157, text="Te buscan en la reja!")

async def start3(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text(f"Hola {update.effective_user.first_name}")
    await context.bot.send_message(chat_id=1589128644, text="Te buscan en la reja!")


#async def echo(update: Update, context: ContextTypes) -> None:
 #   await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    application = ApplicationBuilder().token('5346844231:AAGZ6_aJPPi01TnxGlCg1BLub8w-m3rGX3Q').build()

    
#    echo_handler= MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
        
    start_handler = CommandHandler('001', start)
    start_handler2 = CommandHandler('002', start2)
    start_handler3 = CommandHandler('003', start3)

    application.add_handler(start_handler)
    application.add_handler(CommandHandler("Hola", start))
    application.add_handler(start_handler2)
    application.add_handler(CommandHandler("Hola", start2))
    application.add_handler(start_handler3)
    application.add_handler(CommandHandler("Hola", start3))
#    application.add_handler(start_handler)
 #   application.add_handler(echo_handler)
    
    application.run_polling()