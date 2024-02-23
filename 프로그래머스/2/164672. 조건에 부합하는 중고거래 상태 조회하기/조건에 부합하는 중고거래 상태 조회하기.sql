-- 코드를 입력하세요
SELECT BOARD_ID,	WRITER_ID,	TITLE,	PRICE,
    CASE
        WHEN STATUS = "DONE" THEN "거래완료"
        WHEN STATUS = "RESERVED" THEN "예약중"
        ELSE "판매중"
    END STATUS
FROM USED_GOODS_BOARD
WHERE YEAR(CREATED_DATE) = 2022 AND MONTH(CREATED_DATE) = 10 AND DAY(CREATED_DATE) = 5
ORDER BY BOARD_ID DESC