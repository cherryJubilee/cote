-- 코드를 입력하세요
SELECT c.NAME, c.DATETIME
FROM (SELECT a.NAME, a.DATETIME -- 아직 입양을 못 간 동물 중
        FROM ANIMAL_INS a
        LEFT OUTER JOIN ANIMAL_OUTS b 
          ON a.ANIMAL_ID = b.ANIMAL_ID
       WHERE b.DATETIME IS NULL
       ORDER BY a.DATETIME
    ) c
LIMIT 3;