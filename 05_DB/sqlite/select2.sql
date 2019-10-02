-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age = 30;

-- SELECT * FROM users WHERE age >= 30;

-- SELECT first_name FROM users WHERE age >= 30;

-- SELECT last_name, age FROM users where age >= 30 and last_name = '김' LIMIT 10 ;

-- COUNT
-- SELECT COUNT(*) FROM users;

--AVG, SUM, MIN, MAX(숫자 컬럼에만 가능)
--30살 이상인 사람들의 평균나이
-- SELECT AVG(age) FROM users WHERE age >= 30;

--users 에서 잔액이 가장 높은 사람과 잔액

-- SELECT first_name, MAX(balance) FROM users 

-- SELECT AVG(balance) FROM users WHERE age >= 30;

-- wild cards
-- SELECT * FROM users WHERE country LIKE '경상%';

-- SELECT * FROM users WHERE phone LIKE '%2463%'

-- SELECT age, first_name FROM users ORDER BY age DESC LIMIT 10;

-- SELECT age, balance FROM users
-- ORDER BY age, balance LIMIT 10;

SELECT first_name, last_name From users ORDER BY balance DESC LIMIT 10;