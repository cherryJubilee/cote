-- 코드를 입력하세요
WITH HOURS AS (
    SELECT LEVEL - 1 AS HOUR
    FROM DUAL
    CONNECT BY LEVEL <= 24
)

SELECT 
    h.HOUR,
    NVL(COUNT(a.DATETIME), 0) AS COUNT
FROM HOURS h
LEFT OUTER JOIN ANIMAL_OUTS a
ON h.HOUR = TO_NUMBER(TO_CHAR(a.DATETIME, 'hh24'))
GROUP BY h.HOUR
ORDER BY h.HOUR;
