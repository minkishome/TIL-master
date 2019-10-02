-- SELECT name, age FROM classmates;
-- SELECT id FROM classmates;

-- LIMIT OFFSET

-- SELECT * FROM classmates;
-- SELECT * FROM classmates LIMIT 2;
-- SELECT * FROM classmates LIMIT 1 OFFSET 2;

-- WHERE
-- SELECT * FROM classmates WHERE name = '김지희'
-- SELECT * FROM classmates WHERE name = '김지희' LIMIT 1 이런식으로 모든 김지희 중 하나만

-- DISTINCT
SELECT DISTINCT age FROM classmates;
