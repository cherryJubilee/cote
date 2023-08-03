-- 코드를 입력하세요
SELECT ORDER_ID, 
        PRODUCT_ID,
        TO_CHAR(OUT_DATE, 'yyyy-mm-dd') AS OUT_DATE, 
        CASE
            WHEN TO_CHAR(OUT_DATE, 'mm-dd') > '05-01' THEN '출고대기'
            WHEN TO_CHAR(OUT_DATE, 'mm-dd') <= '05-01' THEN '출고완료'
            ELSE '출고미정'
        END AS 출고여부 
FROM FOOD_ORDER
ORDER BY ORDER_ID