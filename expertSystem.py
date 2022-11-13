from pyswip import Prolog

prolog = Prolog()
prolog.consult("emotionDetect.pl")

for res in prolog.query("helpme."):
    pass   














