-- List tables of a specified database
SET @db_name = @1;
USE @1;
SHOW TABLES;
