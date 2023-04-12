SELECT Doctor, Professor, Singer, Actor
FROM (SELECT OCCUPATION,
     CASE WHEN Occupation = 'Doctor' THEN Name END as Doctor,
     CASE WHEN Occupation = 'Professor' THEN Name END as Professor,
     CASE WHEN Occupation = 'Singer' THEN Name END as Singer,
     CASE WHEN Occupation = 'Actor' THEN Name END as Actor
From OCCUPATIONS) t
GROUP BY Doctor, Professor, Singer, Actor
ORDER BY Doctor, Professor, Singer, Actor;

# 해결중,,