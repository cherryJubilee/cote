-- 코드를 입력하세요
SELECT USER_ID, 
        NICKNAME, 
        CITY || ' ' || STREET_ADDRESS1 || ' ' ||STREET_ADDRESS2, 
        SUBSTR(TLNO, 1, 3) || '-' || SUBSTR(TLNO, 4, 4) || '-' || SUBSTR(TLNO, 8, 4)
FROM USED_GOODS_USER -- 사용자 ID, 닉네임, 전체주소, 전화번호를 조회 가능 테이블 
WHERE USER_ID IN ( SELECT WRITER_ID --  중고 거래 게시물을 3건 이상 등록한 사용자를 비교하기 위한 서브쿼리
                     FROM USED_GOODS_BOARD
                  GROUP BY WRITER_ID
                  HAVING COUNT(WRITER_ID) >= 3
                  )
                  
                  
ORDER BY USER_ID DESC