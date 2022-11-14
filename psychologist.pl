

helpme :-
	write("Tell me, what is your problem?"),nl,
	repeat,
	read_string(user, "\n", "\r", End, M),
	split_string(M," "," ",L),
	saveinto(L),
	makeans(L),
	fail.

makeans(L) :- recognize(L,1),
	write("How long have you felt that way?"),nl,!.

makeans(L) :- recognize(L,2),
	write("Tell me more about your family."),nl,!.

makeans(L) :- recognize(L,3),
	write("Do emotions frighten you?"),nl,!.

makeans(L) :- recognize(L,4),
	write("Please do not use words like that."),nl,!.

makeans(L) :- recognize(L,5),
	write("Please be more explicit."),nl,!.

makeans(L) :- recognize(L,6),
	write("That sound significant."),nl,!.

makeans(L) :- recognize(L,7),
	write("How are you feeling right now?"),nl,!.

makeans(L) :- recognize(L,8),
	write("I am here to solve also this kind of things, don't worry and continue."),nl,!.

%makeans(L) :- recognize(L,9),
	%write("Earlier you mentioned your mother."),nl,!.

makeans(L) :- recognize(L,10),
	write("Tell me more."),nl,!.

% if user feels tired maybe we suggest chill music, something calm (not metal/rock)
makeans(L) :- recognize(L,11),
	write("Are you sleeping well?"),nl,!.

% if user feels agitated maybe we suggest chill music, something calm (not metal/rock)
makeans(L) :- recognize(L,12),
	write("Don't worry, we can solve this."),nl,!.

recognize(L,1) :- member("feel",L).
recognize(L,2) :- member("mother",L). %assert(mother).
recognize(L,3) :- member("love",L).
recognize(L,4) :- member("hell",L).
recognize(L,5) :- L = ["yes"] ; L = ["no"].
recognize(L,6) :- member("sex",L).
recognize(L,7) :- member("sadness",L); member("anger",L).
recognize(L,8) :- member("complex",L).
%recognize(_,9) :- mother. % for repeating if mother is in the database
recognize(_,10). % for Tell me more.
recognize(L,11) :- member("tired",L); member("sleep",L).
recognize(L,12) :- member("agitated",L); member("panic",L).

saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	write(Out, L),
	nl(Out),
	close(Out).





