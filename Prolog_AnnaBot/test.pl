
%call this on python with helpme(S,"I feel sad").

helpme(S,M) :-
	split_string(M," "," ",L),
	makeans(L,S).

makeans(L,"How long have you felt that way?") :- recognize(L,1).

recognize(L,1) :- member("sad",L).





