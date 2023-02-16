SELECT * FROM payments;
-- amount 의 최대값으로 고객 번호를 찾아야함
-- SELECT MAX(amount)
-- FROM payments;
-- WHERE amount = 위에서 찾은 최대 값

SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
    FROM payments
);
