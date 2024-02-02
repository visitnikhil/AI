can_fly(sparrow).
can_fly(pigeon).
can_fly(albatross).
can_fly(eagle).

bird_can_fly(X) :-
    can_fly(X),
    write(X),
    write(' can fly'), nl.

bird_can_fly(X) :-
    \+can_fly(X),
    write(X),
    write(' cannot fly'), nl.
