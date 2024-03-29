-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
FROM PATIENT p
JOIN APPOINTMENT a ON p.PT_NO = a.PT_NO
JOIN DOCTOR d ON a.MDDR_ID = d.DR_ID
WHERE TO_CHAR(a.APNT_YMD, 'yyyy-mm-dd') = '2022-04-13'
AND a.MCDP_CD = 'CS'
AND a.APNT_CNCL_YN = 'N'
ORDER BY a.APNT_YMD;
