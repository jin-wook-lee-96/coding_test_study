SELECT Start_Date, MIN(End_Date)
FROM 
    (SELECT Start_Date 
     FROM Projects
     WHERE Start_Date NOT IN (SELECT End_date
                                FROM Projects)) a,
    (SELECT End_date
     FROM Projects 
     WHERE End_Date NOT IN (SELECT Start_Date
                              FROM Projects)) b
WHERE Start_date < End_Date
GROUP BY Start_Date
ORDER BY ABS(TRUNC(MIN(End_Date)- Start_Date)), Start_date;