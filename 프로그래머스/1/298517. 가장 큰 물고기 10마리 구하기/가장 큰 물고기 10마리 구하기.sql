-- 가장 큰 물고기 10마리의 id,length -> 길이 내림차순, id 오름차순
SELECT
ID,
LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID ASC
LIMIT 10
