

%starting predicate
helpme(S,M) :-
	split_string(M," "," ",L),
	makeans(L,S).

makeans(L,"How long have you felt that way?$gen_sad") :- recognize(L,1),!.
makeans(L,"Tell me more about your family.") :- recognize(L,2),!.
makeans(L,"Earlier you mentioned your mother.") :- recognize(L,99), retract(mother),!.
makeans(L,"Tell me more.") :- recognize(L,100),!.


recognize(L,1) :- member("sad",L).
recognize(L,2) :- member("mother",L), assertz(mother).
recognize(_,99) :- mother.
recognize(_,100). 




