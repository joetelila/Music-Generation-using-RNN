
common_member(L1,L2) :-
	member(E,L1),
	member(E,L2).

read_KB(K) :-
    csv_read_file("country.csv", Rows, [separator(0';)]),
    maplist(arg(1), Rows, Names),
    maplist(atom_string, Names, K).


%starting predicate
helpme(S,M) :-
	split_string(M," "," ",L),
	makeans(L,S).

makeans(L,"How long have you felt that way?$gen_sad") :- recognize(L,1).
makeans(L,"Tell me more about your family.") :- recognize(L,2).
makeans(L,"Do emotions frighten you?") :- recognize(L,3).
makeans(L,"Please do not use words like that.") :- recognize(L,4).
makeans(L,"Please be more explicit.") :- recognize(L,5).
makeans(L,"That sound significant.") :- recognize(L,6).
makeans(L,"How are you feeling right now?") :- recognize(L,7).
makeans(L,"Don't worry, go on.") :- recognize(L,8).
%makeans(L,"Earlier you mentioned your mother.") :- recognize(L,9).
makeans(L,"Don't worry, we can solve this.") :- recognize(L,10).
makeans(L,"Are you sleeping well these days?") :- recognize(L,11).
makeans(L,"Good! what makes you feel happy?$gen_happy") :- recognize(L,12).
makeans(L,"Just calm down and tell me what makes you angry.") :- recognize(L,13).
makeans(L,"Which country do you choose?") :- recognize(L,14).
makeans(L,"How many days did you stay?") :- recognize(L,15).
makeans(L,"Do you like travelling by plane?") :- recognize(L,16).
makeans(L,"Precisely, which tought makes you unconfortable?") :- recognize(L,17).
makeans(L,"You know, also pilots can have fear to fly. It is a very common thing and we'll figure it out. Go on.") :- recognize(L,18).
makeans(L,"Every human being experiences fear, what makes you feel this way?") :- recognize(L,19).
makeans(L,"I understand. What is the name of your friend?") :- recognize(L,20).
makeans(L,"Tell me more about your friends.") :- recognize(L,21).
makeans(L,"Okay. When you have panic toughts, the first thing you have to do is beathe slowly. Then, you may try to feel the environment around you, understanding that there are no changes. Now, go on.") :- recognize(L,22).
makeans(L,"What tought makes you feel disgusted") :- recognize(L,23).
makeans(L,"Why are you surprised") :- recognize(L,24).
makeans(L,"I am just a machine, but I can strongly suggest to consult a psychologist for a therapy.") :- recognize(L,25).
makeans(L,"Tell me more.") :- recognize(L,100).


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
recognize(L,12) :- member("happy",L).
recognize(L,13) :- member("angry",L).
recognize(L,14) :- member("trip",L).
%reads an external KB, if has common element with the user input, goes on with the chat
recognize(L,15) :- 
	read_KB(K),
	common_member(K,L).
recognize(L,16) :- member("plane",L).
recognize(L,17) :- member("unconfortable",L). 
recognize(L,18) :- member("fear",L), member("fly",L).
recognize(L,19) :- member("I",L), member("have",L), member("fear",L).
recognize(L,20) :- member("not",L), member("friends",L), member("anymore",L).
recognize(L,21) :- member("friends",L); member("friend",L).
recognize(L,22) :- member("panic",L).
recognize(L,23) :- member("disgust",L).
recognize(L,24) :- member("surprise",L).
recognize(L,25) :- member("solve",L).
recognize(_,100). 




