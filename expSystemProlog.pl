% INFO: assert: assert a rule or fact into database


% chat with user 
chat :-
    ask("y").

% ask the user how he/she feel, then suggest a genre based on a emotion (optional)
ask("y") :-
     write('How do you feel?: '),
     read_string(user, "\n", "\r", End, E),
     %assert(emotion(E)), %assert a fact or rule into database
     suggest(emotion(E)),
     write("Continue: (y or n) "),
     read_string(user, "\n", "\r", End, Respond),
     ask(Respond).


% The user type "n", hence computing and writing results into file
ask("n") :- 
    tell('/Users/dylan/Desktop/output.txt'), 
    %listing(emotion/1), 
    listing(genre/2),  %lookup result of genre/2 into database
    told.


% predicates which asserts a genre based on emotion
suggest(emotion("sad")) :- assertz(genre(["jazz,classical"],emotion("sad"))).
suggest(emotion("happy")) :- assertz(genre(["pop,country"],emotion("happy"))).




