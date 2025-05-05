-- ON_SALE에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 id와 제품 id출력
-- 회원id 기준 오름차순, 회원id가 같다면 상품 id 기준 내림차순
SELECT
USER_ID,
PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC