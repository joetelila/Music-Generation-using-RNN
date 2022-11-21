from telegram import *
from telegram.ext import * 
from requests import *

updater = Updater(token="5693702383:AAFuKkrPlxNfuC_1O8eyEzoZBMq2nyn75wk")
dispatcher = updater.dispatcher

#To-Do:
#1. How to transfer list to Yohannis (in the readCommand)
#2. Yohannis has to activate the start coammand after song generation (sending /start in the chat would be good)
#3. How does Dylan can activate the startcommand (sending /read in the chat would be a solution)

#With the variables i collect data for:
#1. Measure how many new tries are in the average needed until there is a like.
#So collect every new try counter before it is set to zero (new_tries_list). And make a average out of the elements in the list. 
#2. Measure how many songs are heared again vs. how many songes ended
#3. Measure how many likes and dislkes exits over all played songs.  

new_tries = []
likes = 0
dislikes = 0
new_try_counter = 0
hear_again_counter = 0
song_ended_counter = 0


#This command is activated by user (admin).
#It should create a measure file, where all the values from 1-3 (see above) are inserted.
def measureCommand(update: Update, context: CallbackContext): 
     context.bot.send_message(chat_id=update.effective_chat.id, text="I generated a measurement file")
     with open("example.txt", "w") as f:
              f.write("Number of all likes: " + str(likes) + '\n')
              f.write("Number of all dislikes: " + str(dislikes)+ '\n')
              f.write("Percentage of songs heared again:" + str((hear_again_counter / song_ended_counter)* 100) + '\n')
              f.write("Number of new tries:" + str(new_tries))
 

#While the song is playing ask the user if he likes the song.
def startCommand(update: Update, context: CallbackContext):
     buttons_vote = [[KeyboardButton("👍", callback_data="yes")], [KeyboardButton("👎", callback_data="no")]]
     context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(keyboard = \
     buttons_vote, one_time_keyboard =True), text="Here is your song. Do you like the song?")

#This command is activated by Dylan after collecting the users choice.
#It should then read the choice out of the txt file in a list ['word', 'word']and transfer it to Yohannis.
#He then generates and plays the song and ask for opinion (startcommand)
def readCommand(update: Update, context: CallbackContext):
     with open('choice.txt') as f:
          lines = f.read().splitlines()
          print(lines)
     startCommand(update, context)


#When the song has ended (after full play of hear again or like this command is activated by Yohannis.
#Asks if the user wants to hear the song again or a new choice of emotions or a new generation with the same emotions.
def endedCommand(update: Update, context: CallbackContext): 
    global song_ended_counter
    song_ended_counter = song_ended_counter + 1
    buttons_vote = [[KeyboardButton("hear song again", callback_data="hear again")], [KeyboardButton("new choice of keywords", \
    callback_data="new choice of keywords")], [KeyboardButton("same keywords", callback_data="same keywords")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(keyboard = buttons_vote, one_time_keyboard =True), \
    text="The song has ended. What do you want to do?")

    
def messageHandler(update: Update, context: CallbackContext):
    global likes, dislikes, new_tries, song_ended_counter, hear_again_counter, new_try_counter
    user_input = update.message.text

    #If user disliked the song.
    #Ask the user if he wants to choose other emotions or a new generation with the same emotions.
    if "👎" in user_input:
        dislikes +=1
        print(f"likes => {likes} and dislikes => {dislikes}")
        buttons_do_better = [[KeyboardButton("new choice of keywords", callback_data="new choice of keywords")], \
        [KeyboardButton("same keywords", callback_data="same keywords")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons_do_better), \
        text="Oh I am sorry. Do you want to choose other keywords or try a new song with the same keywords?")

    #If user likes the song
    if "👍" in user_input:
        likes +=1
        print(f"likes => {likes} and dislikes => {dislikes}")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Great!")

    #If user wants to hear the song again.
    #Activate Yohannis who should play the song. Therefore Yohannis has to store the last song.
    if "hear song again" in user_input:
        song_ended_counter = song_ended_counter + 1 #because old song ended
        hear_again_counter = hear_again_counter + 1 #because song is played again
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Yohannis is activated somehow and plays the same song")


    #If user wants to choose other emotions then activate Dylan. Activate Yohannis to stop the song.
    #Dylan than collects new emotions and activates the readcommand.
    if "new choice of keywords" in user_input:
        new_tries.append(new_try_counter)
        new_try_counter = 0 #because then a new song is generated
        song_ended_counter = song_ended_counter + 1 #because old song ended
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Activate Yohannis to stop the song. Dylan is activated somehow and asks for new emotions")

    #If user wants another generation with the same emotions. Yohannis should stop the song. 
    #Send emotions to Yohannis again (readcommand)
    if "same keywords" in user_input:
        new_try_counter = new_try_counter + 1 #because emotions are the same
        song_ended_counter = song_ended_counter + 1 #because old song ended
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Yohannis is activated and stops the song and generates a new song. The song is played.")
        readCommand (update, context)
         
             

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(CommandHandler("measure", measureCommand))
dispatcher.add_handler(CommandHandler("ended", endedCommand))
dispatcher.add_handler(CommandHandler("read", readCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()

# uses code from: https://github.com/isammour/Telegram-Bot-With-Python/blob/main/bot.py
