WITH PARENT AS (
    SELECT ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
),
CHILD AS (
    SELECT ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IN (SELECT ID FROM PARENT)
)
SELECT
ID
FROM ECOLI_DATA
WHERE PARENT_ID IN (SELECT ID FROM CHILD)
ORDER BY ID
