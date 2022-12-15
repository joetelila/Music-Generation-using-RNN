

from pyswip import Prolog
prolog = Prolog()
prolog.consult("psychologist.pl")
list(prolog.query("chat."))