import time
from telegram import *
from telegram.ext import * 
import telegram
from requests import *
# import pyswig
from pyswip import Prolog
from music_generator import MusicGenerator
updater = Updater(token="5693702383:AAFuKkrPlxNfuC_1O8eyEzoZBMq2nyn75wk")
dispatcher = updater.dispatcher

bot_commands = ["start","👍","👎","Generate another song"] 
likes = 0
dislikes = 0
new_try_counter = 0
song_counter = 0
curr_emotion = ""

#Reads from a file called name
#Return: a list l containing the rows in the file  
def readFile(name,l):
    f = open(name, "r")
    l = f.read()
    #print(l)
    return l

# consults the prolog file
prolog = Prolog()
prolog.consult("prolog/collectEmotionsTWO.pl")


# Music generator.
sound_font_path = "/Users/JoeKifle/Documents/EDU/Pisa_2020_2021/Semester_1/AIF_22/Music-Generation-using-RNN/soundfont/FluidR3_GM.sf2"
sampling_rate = 16000
model_path = "models/model.h5"
mus_gen = MusicGenerator(model_path, sampling_rate, sound_font_path)

#This command is activated by user (admin).
#It should create a measure file, where all the values from 1-3 (see above) are inserted.
def measureCommand(update: Update, context: CallbackContext): 
     context.bot.send_message(chat_id=update.effective_chat.id, text="I generated a measurement file")
 
#Ask for bad or happy if the user decides that he wants a song based on new emotions
def askAgain(update: Update, context: CallbackContext):
    buttons_vote = [[KeyboardButton("Sad", callback_data="sad")], [KeyboardButton("Happy", callback_data="happy")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(keyboard = buttons_vote, one_time_keyboard =True), text="Choose a new emotion")

#This command transfers the user wish to the music generator
#While the song is playing ask the user if he likes the song with buttons
def startCommand(update: Update, context: CallbackContext):
     #-----TODO----- transfer emotions list to Yoannis 
     buttons_vote = [[KeyboardButton("👍", callback_data="yes")], [KeyboardButton("👎", callback_data="no")]]
     context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(keyboard = buttons_vote, one_time_keyboard =True), text="Here is your song. Do you like the song?")
        
def messageHandler(update: Update, context: CallbackContext):
    global likes, dislikes, new_tries, song_counter, new_try_counter,curr_emotion
    user_input = update.message.text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    if user_input not in bot_commands:
        _query = "helpme(S,'"+str(user_input)+"')."
        query_res = list(prolog.query(_query))
        for _res in query_res:
            _temp_res = _res['S'].decode('utf8').split("$")

            if len(_temp_res)>1:
                curr_emotion = _temp_res[1]
                print("Generating song with emotion: "+curr_emotion)
                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.RECORD_AUDIO)
                music_midi = mus_gen.generate(_temp_res[0], 100)
                music_audio = mus_gen.convert_to_audio(music_midi)
                context.bot.send_voice(chat_id=update.effective_chat.id, voice=open(music_audio, 'rb'))
                song_counter = song_counter + 1
                startCommand(update, context)
            context.bot.send_message(chat_id=update.effective_chat.id, text=_res['S'].decode('utf8'))
            
            #context.bot.send_message(chat_id=update.effective_chat.id, text=_res["S"])
            #break
            
    #Ask the user if he wants to choose other emotions or a new generation with the same emotions.
    if "👎" in user_input:
        dislikes +=1
        print(f"likes => {likes} and dislikes => {dislikes}")
        buttons_do_better = [ [KeyboardButton("Generate another song", callback_data="Generate another song")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons_do_better), text="Do you want to generate a new song with the same emotion?, or Tell me more.")
        #If user likes the song
    if "👍" in user_input:
        likes +=1
        print(f"likes => {likes} and dislikes => {dislikes}")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Great!")


    #If user wants another generation with the same emotions
    #Music generator generates another song
    #Play the song
    if "Generate another song" in user_input:
        new_try_counter = new_try_counter + 1 #because emotions are the same
        context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('test_auid.wav', 'rb'))
        context.bot.send_message(chat_id=update.effective_chat.id, text="Here is your song with the same emotion, "+curr_emotion)
        song_counter = song_counter + 1
        startCommand(update, context)
       
    #If user wants the measured performance values
    if "measurement" in user_input:
         context.bot.send_message(chat_id=update.effective_chat.id, text="I generated a measurement file")
         with open("example.txt", "w") as f:
              f.write("Number of all likes: " + str(likes) + '\n')
              f.write("Number of all dislikes: " + str(dislikes)+ '\n')
              f.write("Percentage of all new tries: "+str((new_try_counter / (likes + dislikes))* 100) + '\n')
              f.write("Number of all new tries: " + str(new_try_counter))

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()


# uses code from: https://github.com/isammour/Telegram-Bot-With-Python/blob/main/bot.py
