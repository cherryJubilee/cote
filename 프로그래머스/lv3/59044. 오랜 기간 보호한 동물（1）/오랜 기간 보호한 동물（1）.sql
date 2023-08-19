-- 코드를 입력하세요
-- 가장 오래 보호소에 있었던 동물 3마리 이름과 보호시작일
SELECT c.NAME, c.DATETIME
FROM (SELECT a.NAME, a.DATETIME -- 아직 입양을 못 간 동물 중
        FROM ANIMAL_INS a
        LEFT OUTER JOIN ANIMAL_OUTS b 
          ON a.ANIMAL_ID = b.ANIMAL_ID
       WHERE b.DATETIME IS NULL
      ORDER BY a.DATETIME
    ) c
WHERE ROWNUM <= 3
