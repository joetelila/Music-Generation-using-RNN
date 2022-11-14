from pyswip import Prolog

prolog = Prolog()
prolog.consult("psychologist.pl")

for res in prolog.query("helpme."):
    pass   














