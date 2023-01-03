from pyswip import Prolog


prolog = Prolog()

prolog.consult("Music-Suggestion-Expert-System.pl")

res = list(prolog.query("suggest(Song)"))

print(res)

