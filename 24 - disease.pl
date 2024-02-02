

diet_suggestion(diabetes, 'Foods to avoid: sugary beverages, processed grains, and high-sugar fruits. Foods to consume: non-starchy vegetables, whole grains, lean proteins, and healthy fats.').


suggest_diet_for_disease(Disease) :-
    diet_suggestion(Disease, Diet),
    write('For '), write(Disease), write(' patients, the suggested diet is:'), nl,
    write(Diet), nl.


?- suggest_diet_for_disease(diabetes).
