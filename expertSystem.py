from pyswip import Prolog

prolog = Prolog()
prolog.consult("expSystemProlog.pl")

for res in prolog.query("chat."):
    pass   














