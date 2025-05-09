WITH TBL AS (
    SELECT
        FOOD_TYPE,
        MAX(FAVORITES) AS FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)

SELECT
    I.FOOD_TYPE,
    I.REST_ID,
    I.REST_NAME,
    I.FAVORITES
FROM REST_INFO I
JOIN TBL
  ON I.FOOD_TYPE = TBL.FOOD_TYPE
 AND I.FAVORITES = TBL.FAVORITES
ORDER BY I.FOOD_TYPE DESC