

chat :- 
	write("Tell me everything."),nl,
	helpme("y").

helpme("n").
helpme("y") :-
	read_string(user, "\n", "\r", End, M),
	split_string(M," "," ",L),
	makeans(L,R),
	saveinto(L),
	helpme(R).


makeans(L,"y") :- recognize(L,1),
	write("How long have you felt that way?"),nl,!.

makeans(L,"y") :- recognize(L,2),
	write("Tell me more about your family."),nl,!.

makeans(L,"y") :- recognize(L,3),
	write("Do emotions frighten you?"),nl,!.

makeans(L,"y") :- recognize(L,4),
	write("Please do not use words like that."),nl,!.

makeans(L,"y") :- recognize(L,5),
	write("Please be more explicit."),nl,!.

makeans(L,"y") :- recognize(L,6),
	write("That sound significant."),nl,!.

makeans(L,"y") :- recognize(L,7),
	write("How are you feeling right now?"),nl,!.

makeans(L,"y") :- recognize(L,8),
	write("Don't worry, go on."),nl,!.

%makeans(L,"y") :- recognize(L,9),
	%write("Earlier you mentioned your mother."),nl,!.

makeans(L,"y") :- recognize(L,10),
	write("Don't worry, we can solve this."),nl,!.

% if user feels tired maybe we suggest chill music, something calm (not metal/rock)
makeans(L,"y") :- recognize(L,11),
	write("Are you sleeping well these days?"),nl,!.

makeans(L,"y") :- recognize(L,12),
	write("Good! what makes you feel happy?"),nl,!.

makeans(L,"y") :- recognize(L,13),
	write("Just calm down and tell me what makes you angry."),nl,!.

makeans(L,"y") :- recognize(L,14),
	write("Which country do you choose?"),nl,!.

makeans(L,"y") :- recognize(L,15),
	write("How many days did you stay?"),nl,!.

makeans(L,"y") :- recognize(L,16),
	write("Do you like travelling by plane?"),nl,!.

makeans(L,"y") :- recognize(L,17),
	write("Precisely, which tought makes you unconfortable?"),nl,!.

makeans(L,"y") :- recognize(L,18),
	write("You know, also pilots can have fear to fly. It is a very common thing and we'll figure it out. Go on."),nl,!.

makeans(L,"y") :- recognize(L,19),
	write("Every human being experiences fear, what makes you feel this way?"),nl,!.

makeans(L,"y") :- recognize(L,20),
	write("I understand. What is the name of your friend?"),nl,!.

makeans(L,"y") :- recognize(L,21),
	write("Tell me more about your friends."),nl,!.

makeans(L,"y") :- recognize(L,22),
	write("Okay. When you have panic toughts, the first thing you have to do is beathe slowly. Then, you may try to feel the environment around you, understanding that there are no changes. Now, go on."),nl,!.

makeans(L,"y") :- recognize(L,23),
	write("What tought makes you feel disgusted'"),nl,!.

makeans(L,"y") :- recognize(L,24),
	write("Why are you surprised'"),nl,!.

makeans(L,"y") :- recognize(L,25),
	write("I am just a machine, but I can strongly suggest to consult a psychologist for a therapy.'"),nl,!.


makeans(L,"n") :- recognize(L,99),
	write("Quit").

makeans(L,"y") :- recognize(L,100),
	write("Tell me more."),nl,!.




recognize(L,1) :- member("sad",L).
recognize(L,2) :- member("mother",L). %assert(mother).
recognize(L,3) :- member("love",L).
recognize(L,4) :- member("hell",L).
recognize(L,5) :- L = ["yes"] ; L = ["no"].
recognize(L,6) :- member("sex",L).
recognize(L,7) :- member("sadness",L); member("anger",L).
recognize(L,8) :- member("complex",L).
%recognize(_,9) :- mother. % for repeating if mother is in the database
recognize(L,10) :- member("tired",L); member("sleep",L).
recognize(L,11) :- member("agitated",L).
recognize(L,12) :- member("I",L), member("feel",L), member("happy",L).
recognize(L,13) :- member("I",L), member("feel",L), member("angry",L).
recognize(L,14) :- member("trip",L).
recognize(L,15) :- 
	member("America",L);
	member("Italy",L);
	member("France",L);
	member("Spain",L);
	member("China",L);
	member("Japan",L);
	member("Russia",L).

recognize(L,16) :- member("plane",L).
recognize(L,17) :- member("unconfortable",L). 
% fear for plane
recognize(L,18) :- member("fear",L), member("fly",L).
% fear in general
recognize(L,19) :- member("I",L), member("have",L), member("fear",L).
% fear for friendship
recognize(L,20) :- member("not",L), member("friends",L), member("anymore",L).
recognize(L,21) :- member("friends",L); member("friend",L).
recognize(L,22) :- member("panic",L).
recognize(L,23) :- member("disgust",L).
recognize(L,24) :- member("surprise",L).
recognize(L,25) :- member("solve",L).

recognize(L,99) :- member("quit",L);member("exit",L).
recognize(_,100). % for Tell me more.


saveinto(_).
saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	member("sad",L),
	write(Out, "sad"),
	nl(Out),
	close(Out).

saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	member("angry",L),
	write(Out, "angry"),
	nl(Out),
	close(Out).

saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	member("happy",L),
	write(Out, "happy"),
	nl(Out),
	close(Out).

saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	member("fear",L),
	write(Out, "fear"),
	nl(Out),
	close(Out).

saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	member("disgust",L),
	write(Out, "disgust"),
	nl(Out),
	close(Out).

saveinto(L) :-
	open('/Users/dylan/Desktop/emotions.txt', append, Out),
	member("surprise",L),
	write(Out, "surprise"),
	nl(Out),
	close(Out).




