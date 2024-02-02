/* Facts */
male(john).
male(mike).
male(jack).
female(jane).
female(lisa).
parent(john, mike).
parent(jane, mike).
parent(john, lisa).
parent(jane, lisa).
parent(mike, jack).
parent(lisa, jack).

/* Rules */
father(Father, Child) :- male(Father), parent(Father, Child).
mother(Mother, Child) :- female(Mother), parent(Mother, Child).
sibling(Person1, Person2) :- parent(P, Person1), parent(P, Person2), Person1 \= Person2.
brother(Person, Sibling) :- male(Person), sibling(Person, Sibling).
sister(Person, Sibling) :- female(Person), sibling(Person, Sibling).
grandparent(Grandparent, Grandchild) :- parent(Grandparent, Parent), parent(Parent, Grandchild).
ancestor(Ancestor, Descendant) :- parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :- parent(P, Descendant), ancestor(Ancestor, P).
