SELECT Name || '(' || SUBSTR(Occupation,1,1) || ')' as Name
FROM OCCUPATIONS
ORDER BY Name ASC;
SELECT 'There are a total of ' || COUNT(Occupation)||' '|| LOWER(Occupation) || 's.' as result
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY result;