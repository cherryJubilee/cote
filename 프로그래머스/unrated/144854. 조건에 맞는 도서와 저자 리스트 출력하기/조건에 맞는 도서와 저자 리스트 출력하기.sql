-- 코드를 입력하세요
SELECT 
    a.BOOK_ID, 
    b.AUTHOR_NAME, 
    TO_CHAR(a.PUBLISHED_DATE, 'yyyy-mm-dd') AS published_date
FROM BOOK a
JOIN AUTHOR b ON a.AUTHOR_ID = b.AUTHOR_ID
WHERE a.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE