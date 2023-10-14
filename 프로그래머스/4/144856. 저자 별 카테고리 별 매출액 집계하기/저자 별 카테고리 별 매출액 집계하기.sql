-- 코드를 입력하세요
SELECT
    a.AUTHOR_ID,
    b.AUTHOR_NAME,
    a.CATEGORY,
    SUM(a.PRICE * c.SALES) AS TOTAL_SALES
    
FROM BOOK a
JOIN AUTHOR b ON a.AUTHOR_ID = b.AUTHOR_ID
JOIN BOOK_SALES c ON a.BOOK_ID = c.BOOK_ID

WHERE TO_CHAR(c.SALES_DATE, 'yyyy-mm') = '2022-01'
GROUP BY a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY
              
ORDER BY 1, 3 DESC