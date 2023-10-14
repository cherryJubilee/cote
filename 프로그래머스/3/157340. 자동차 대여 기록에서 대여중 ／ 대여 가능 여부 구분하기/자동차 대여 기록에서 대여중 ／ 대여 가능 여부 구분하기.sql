SELECT car_id, MAX(availability) AS availability
    
FROM 
    (SELECT  
        CAR_ID,
        CASE
            WHEN TO_CHAR(START_DATE, 'yyyy-mm-dd') <= '2022-10-16' 
            AND TO_CHAR(END_DATE, 'yyyy-mm-dd') >= '2022-10-16'  THEN '대여중'
            ELSE '대여 가능'
        END AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY)
GROUP BY car_id
ORDER BY 1 DESC