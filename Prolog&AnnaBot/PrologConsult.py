from pyswip import Prolog

def startPsychologist():
    prolog = Prolog()
    prolog.consult("psychologist.pl")
    l = list(prolog.query("chat."))