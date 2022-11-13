from telegram import *
from telegram.ext import * 
from requests import *

updater = Updater(token="5693702383:AAFuKkrPlxNfuC_1O8eyEzoZBMq2nyn75wk")
dispatcher = updater.dispatcher

selecting = []
likes = 0
dislikes = 0
 


def startCommand(update: Update, context: CallbackContext):
    selecting = []
    buttons_start = [[KeyboardButton("sad")], [KeyboardButton("happy")],  [KeyboardButton("love")],  [KeyboardButton("fear")],  [KeyboardButton("slow")],  [KeyboardButton("fast")], [KeyboardButton("I finished my choice")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Let me generate some music for you! What kind of music do you want to hear? You can choose multiple keywords", reply_markup=ReplyKeyboardMarkup(buttons_start))

def messageHandler(update: Update, context: CallbackContext):
    global selecting
    global likes, dislikes
    user_input = update.message.text

    if checkEmotionInput(user_input) == True:
        selecting.append(user_input)
        print(selecting)
    
    if "I finished my choice" in user_input or "same keywords" in user_input:
        selecting = []
        buttons_vote = [[KeyboardButton("👍", callback_data="yes")], [KeyboardButton("👎", callback_data="no")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(keyboard = buttons_vote, one_time_keyboard =True), text="Here is your song! Do you like it?")

    if "👎" in user_input:
        dislikes +=1
        print(f"likes => {likes} and dislikes => {dislikes}")
        buttons_do_better = [[KeyboardButton("new choice of keywords", callback_data="new choice of keywords")], [KeyboardButton("same keywords", callback_data="same keywords")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons_do_better), text="Oh I am sorry. Do you want to choose other keywords or try a new song with the same keywords?")
    
    if "👍" in user_input:
        likes +=1
        print(f"likes => {likes} and dislikes => {dislikes}")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Great!")
        
    if "new choice of keywords" in user_input:
        startCommand(update, context)

def checkEmotionInput (user_input):
    if "sad" in user_input or "happy" in user_input or "love" in user_input or "fear" in user_input or "slow" in user_input or "fast" in user_input:
        return True
    else:
        return False

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()

# uses code from: https://github.com/isammour/Telegram-Bot-With-Python/blob/main/bot.py
