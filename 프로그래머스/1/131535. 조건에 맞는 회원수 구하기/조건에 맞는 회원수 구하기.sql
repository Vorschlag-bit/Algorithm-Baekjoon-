-- 2021년에 가입한 회원 중 20 <= 나이 <= 29 회원 개수
SELECT
COUNT(*) AS USERS
FROM USER_INFO
WHERE JOINED LIKE '2021%' AND AGE >= 20 AND AGE <= 29