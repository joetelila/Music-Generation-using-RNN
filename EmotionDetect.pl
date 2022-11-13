

helpme :-
	write("Tell me, what is your problem?"),nl,
	repeat,
	read_string(user, "\n", "\r", End, M),
	split_string(M," "," ",L),
	makeanswer(L),
	saveinto(L),
	fail.

makeanswer(L) :- recognize(L,1),
	write("How long have you felt that way?"),nl,!.

makeanswer(L) :- recognize(L,2),
	write("Tell me more about your family."),nl,!.

makeanswer(L) :- recognize(L,3),
	write("Do emotions frighten you?"),nl,!.

makeanswer(L) :- recognize(L,4),
	write("Please do not use words like that."),nl,!.

makeanswer(L) :- recognize(L,5),
	write("Please be more explicit."),nl,!.

makeanswer(L) :- recognize(L,6),
	write("That sound significant."),nl,!.

makeanswer(L) :- recognize(L,7),
	write("How are you feeling right now?"),nl,!.

makeanswer(L) :- recognize(L,8),
	write("Too many mind games."),nl,!.

%makeanswer(L) :- recognize(L,9),
	%write("Earlier you mentioned your mother."),nl,!.

makeanswer(L) :- recognize(L,10),
	write("Tell me more."),nl,!.


recognize(L,1) :- member("i",L); member("feel",L).
recognize(L,2) :- member("mother",L). %assert(mother).
recognize(L,3) :- member("love",L).
recognize(L,4) :- member("hell",L).
recognize(L,5) :- L = ["yes"] ; L = ["no"].
recognize(L,6) :- member(["sex"],L).
recognize(L,7) :- member(["sadness"],L); member(["anger"],L).
recognize(L,8) :- member(["complex"],L); member(["fixation"],L).
%recognize(_,9) :- mother. % for repeating if mother is in the database
recognize(_,10). % for Tell me more.

saveinto(L) :- 
	open('/Users/dylan/Desktop/emotions.txt',append,Out),
	member("sad",L),
	write(Out,"sad"),
	nl(Out),
	close(Out).

saveinto(L) :- 
	open('/Users/dylan/Desktop/emotions.txt',append,Out),
	member("happy",L),
	write(Out,"happy"),
	nl(Out),
	close(Out).





