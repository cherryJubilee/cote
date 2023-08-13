-- 코드를 입력하세요
 SELECT CAR_ID, MAX(AVAILABILITY) AS AVAILABILITY
 FROM (
    SELECT CAR_ID, 
            START_DATE,
            END_DATE, 
            CASE
                WHEN TO_CHAR(START_DATE, 'yyyy-mm-dd') <= '2022-10-16' 
                AND '2022-10-16' <= TO_CHAR(END_DATE, 'yyyy-mm-dd') THEN '대여중'
                ELSE '대여 가능'
            END AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
 )
GROUP BY CAR_ID       
ORDER BY CAR_ID DESC;