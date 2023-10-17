-- Display top 3 cities' temperatures during July and August
SELECT city, temperature FROM temperatures WHERE (MONTH(date) = 7 OR MONTH(date) = 8) ORDER BY temperature DESC LIMIT 3;
