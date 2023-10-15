SELECT a.ANIMAL_ID, a.NAME

FROM ANIMAL_OUTS a
LEFT OUTER JOIN ANIMAL_INS b ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL

ORDER BY 1