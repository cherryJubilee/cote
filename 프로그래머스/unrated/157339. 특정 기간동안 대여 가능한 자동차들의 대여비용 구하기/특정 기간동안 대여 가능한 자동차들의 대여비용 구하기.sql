SELECT 
    C.CAR_ID,
    C.CAR_TYPE,
    (C.DAILY_FEE * (1 - (P.DISCOUNT_RATE / 100)) * 30) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR C            
    INNER JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    ON
    C.CAR_TYPE = P.CAR_TYPE
WHERE
    C.CAR_ID 
    NOT IN(
        SELECT
            CAR_ID
        FROM 
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE 
            (CAR_ID, END_DATE) IN(
            SELECT 
                CAR_ID, 
                MAX(END_DATE)
            FROM 
                CAR_RENTAL_COMPANY_RENTAL_HISTORY
            GROUP BY
                CAR_ID)
    AND 
        TO_CHAR(START_DATE, 'YYYYMMDD') <= '20221130'
    AND 
        TO_CHAR(END_DATE, 'YYYYMMDD') >= '20221101')
    AND 
        C.CAR_TYPE IN ('세단', 'SUV')
    AND 
        P.DURATION_TYPE = '30일 이상'
    AND 
        (C.DAILY_FEE * (1 - (P.DISCOUNT_RATE / 100)) * 30) 
        BETWEEN
            500000 AND 2000000
ORDER BY 
    FEE DESC, 
    C.CAR_TYPE, 
    C.CAR_ID DESC;