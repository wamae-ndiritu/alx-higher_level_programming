-- Lists the number of records with the same score i =n second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
