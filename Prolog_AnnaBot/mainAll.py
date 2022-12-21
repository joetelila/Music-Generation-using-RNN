from bot_measure import *
from PrologConsult import startPsychologist

#starts dylan bot
startPsychologist()

dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

#starts Anna bot
updater.start_polling()
