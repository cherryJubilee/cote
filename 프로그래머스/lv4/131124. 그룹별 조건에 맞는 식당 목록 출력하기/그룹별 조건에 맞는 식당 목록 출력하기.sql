-- 코드를 입력하세요
SELECT a.MEMBER_NAME, 
       b.REVIEW_TEXT, 
       TO_CHAR(b.REVIEW_DATE, 'yyyy-mm-dd') AS REVIEW_DATE
FROM MEMBER_PROFILE a
JOIN REST_REVIEW b ON a.MEMBER_ID = b.MEMBER_ID
WHERE a.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM (
        SELECT MEMBER_ID
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY COUNT(*) DESC
    )
    WHERE ROWNUM = 1
)
ORDER BY b.REVIEW_DATE, b.REVIEW_TEXT;
