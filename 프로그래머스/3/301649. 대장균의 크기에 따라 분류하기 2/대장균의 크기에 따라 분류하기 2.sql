WITH RANKED AS (
    SELECT
    ID,
    ROW_NUMBER() OVER(ORDER BY SIZE_OF_COLONY DESC) AS RN
    FROM ECOLI_DATA
),
TOTAL AS (
    SELECT COUNT(*) AS CNT FROM ECOLI_DATA
)
SELECT
    R.ID,
    CASE
        WHEN R.RN <= T.CNT * 0.25 THEN 'CRITICAL'
        WHEN R.RN <= T.CNT * 0.50 THEN 'HIGH'
        WHEN R.RN <= T.CNT * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM RANKED R
JOIN TOTAL T ON 1=1
ORDER BY R.ID ASC;