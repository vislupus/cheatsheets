[MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)    
[String Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)    
[MySQL Basics](https://www.mysqltutorial.org/mysql-basics/)    
[MySQL Tutorial for Beginners](https://www.guru99.com/mysql-tutorial.html)    
[MySQL Tutorial](https://www.w3schools.com/MySQL/default.asp)   
[MySQL Tutorial](https://www.javatpoint.com/mysql-tutorial)   
[LearnSQL](https://learnsql.com/cookbook/)   
[Modern SQL](https://modern-sql.com/)    

```sql
SET @list = '0,1,2,3,4';      
SELECT @list, FIND_IN_SET('1', @list)
SET @list = (SELECT GROUP_CONCAT(id) FROM titanic);
SELECT @list
```

# CREATE TABLE
```sql
CREATE TABLE stocks (
datea TEXT, 
trans TEXT, 
symbol TEXT, 
qty REAL, 
price REAL)
``` 

# INSERT
```sql
INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
INSERT IGNORE INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
``` 

-- UPDATE
UPDATE stocks SET price = 99.99 WHERE qty = 100.0
UPDATE stocks SET countryLabel = 'Italy' WHERE id = 17

-- DELETE
DELETE FROM stocks WHERE price = 99.99
DELETE FROM stocks -- изтриване на всичко

-- Delete columns
ALTER TABLE test
DROP COLUMN start_date, DROP COLUMN end_date;

-- Add columns
ALTER TABLE test ADD COLUMN new_col INT NOT NULL AFTER val;
ALTER TABLE test ADD COLUMN new_col TEXT DEFAULT ""
ALTER TABLE stocks ADD date DATE

-- Check type of column
SELECT typeof(new_col) FROM trip

-- Show all tables in a db
SHOW TABLES;

SHOW COLUMNS FROM titanic;
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='titanic' ORDER BY ordinal_position

-- Describe table
DESCRIBE test;

-- Rename table
RENAME TABLE test TO ren_test;

--- JOIN
SELECT orders.id, orders.product, people.name, people.country FROM orders
INNER JOIN people ON orders.nameID=people.id ORDER BY orders.product DESC;

-- View
CREATE VIEW test_view AS 
SELECT * FROM test WHERE b_num IS NULL;
SELECT * FROM test_view;

-- ORDER BY
ORDER BY id ASC|DESC -- order them by id

SELECT * FROM stocks 
ORDER BY category ASC, name DESC


LIMIT 10 -- limit how many rows to show
GROUP BY category -- group by category

-- Select
SELECT * FROM emag 
SELECT id, item, price_min FROM stocks

SELECT * FROM stocks WHERE symbol = ?
SELECT * FROM stocks WHERE name = "Домати"
SELECT * FROM stocks WHERE price_min = 2345.0

SELECT * FROM stocks WHERE name LIKE "a%" -- започва с а
SELECT * FROM stocks WHERE name LIKE "%y" -- завършва на у
SELECT * FROM stocks WHERE name LIKE "%or%" -- има някъде or
SELECT * FROM stocks WHERE name LIKE "_r%" -- има r на втора позиция
SELECT * FROM stocks WHERE name LIKE "p__%" -- започва с р и има поне три знака
SELECT * FROM stocks WHERE name LIKE "k%e" -- започва с к и завършва на е

SELECT * FROM stocks WHERE category IN ('Цитруси', 'Ядки')

SELECT * FROM stocks WHERE price_min BETWEEN 5 AND 10
SELECT * FROM stocks WHERE price_min>5 AND price_max<10
SELECT * FROM stocks WHERE price_min>5 OR price_max<10
SELECT * FROM stocks WHERE NOT price_max=2
SELECT * FROM stocks WHERE category='Цитруси' AND NOT name='Авокадо'

-- Test for NULL
SELECT * FROM stocks WHERE price_min IS NULL
SELECT * FROM stocks WHERE price_min IS NOT NULL

SELECT DISTINCT product FROM test -- показва всички уникални стойности в тази колона
SELECT COUNT(DISTINCT product) FROM test -- брой уникални стойности в тази колона

SELECT COUNT(*) AS "Count" FROM (
	SELECT DISTINCT product FROM test
) AS "NewData"



-- Functions
MIN(Test)
MAX(Test)
COUNT(Test)
AVG(Test)
SUM(Test)
LENGTH(Test)
COUNT(Test)
IFNULL(Test, "NULL")
IF(Test>10, "MORE", "LESS")



-- CASE
SELECT quantity,
CASE
    WHEN quantity > 30 THEN 'The quantity is greater than 30'
    WHEN quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM test;


SELECT first_name, product, country
FROM test
ORDER BY
(CASE
    WHEN product IS NULL THEN country
    ELSE product
END);


SELECT quantity,
CASE
    WHEN quantity IS NOT NULL THEN "greater than null"
    ELSE "null"
END AS NullText 
FROM test;



--- DATE
SELECT * FROM test WHERE start_date >= end_date;
SELECT * FROM test WHERE start_date > '2015-08-01' AND end_date < '2020-01-01';
SELECT * FROM test WHERE start_date BETWEEN '2015-01-01' AND '2017-01-01';
SELECT * FROM test WHERE EXTRACT(YEAR FROM start_date) = '2015';

SELECT
  DISTINCT EXTRACT(YEAR FROM start_date) AS "Year",
  SUM(quantity*price) OVER(PARTITION BY EXTRACT(YEAR FROM start_date)) AS money_earned
FROM test;



--- GROUP BY
SELECT 
	product, 
	COUNT(*) AS "Count",
	SUM(quantity) AS "Total quantity", 
	MIN(quantity) AS "Minimum quantity", 
	MAX(quantity) AS "Maximum quantity", 
	AVG(quantity) AS "Average quantity" 
FROM test

GROUP BY product
ORDER BY COUNT(product) ASC;


SELECT
	product,
	EXTRACT(YEAR FROM start_date) as year,
    EXTRACT(MONTH FROM start_date) as month,
    SUM(quantity) AS "Total quantity"
FROM test

GROUP BY 
	product,
	EXTRACT(YEAR FROM start_date), 
	EXTRACT(MONTH FROM start_date)
    
ORDER BY year;


SELECT 
	product,
    COUNT(*) AS "Count",
	Month,
	Year,
	SUM(quantity) AS "Total quantity",
    AVG(quantity) AS "Average quantity"
FROM (
  SELECT 
  	product,
    EXTRACT(MONTH from start_date) as Month,
    EXTRACT(YEAR from start_date) as Year, 
    quantity
  FROM test
) AS Table1

GROUP BY 
	product,
	Month,
	Year


SELECT 
	COUNT(DISTINCT product) AS Product, 
	country  AS "Country"
FROM test 

GROUP BY country HAVING Product >= 4
ORDER BY Product


SELECT DISTINCT product, SUM(1) AS "Sum"
FROM (
	SELECT DISTINCT product, quantity FROM test
) AS Test

GROUP BY product HAVING 1 <= SUM(1);


