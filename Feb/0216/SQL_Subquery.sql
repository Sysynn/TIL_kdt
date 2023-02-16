SELECT * FROM payments;
-- amount 의 최대값으로 고객 번호를 찾아야함
-- SELECT MAX(amount)
-- FROM payments;
-- WHERE amount = 위에서 찾은 최대 값
SELECT * FROM customers;

SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
    FROM payments
);

SELECT * FROM employees;
SELECT * FROM offices;

SELECT officeCode
FROM offices
WHERE country = 'USA';

SELECT lastName, firstName
FROM employees
WHERE officeCode IN
(SELECT officeCode
 FROM offices
 WHERE country = 'USA'
);

SELECT customerName
FROM customers
WHERE customerNumber NOT IN
  (SELECT DISTINCT customerNumber
  FROM orders
  );

SELECT * FROM payments;
  
SELECT customerNumber, amount, contactFirstname
FROM 
(SELECT *
 FROM payments
 INNER JOIN customers
 USING (customerNumber)) AS mySub
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
    );
    
SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (
	SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);

SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS(
	SELECT *
    FROM offices
    WHERE
		city = 'Paris' AND employees.officeCode = offices.officeCode
);    

SELECT contactFirstName, creditLimit,
	CASE  
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
    END AS grade
FROM customers;

SELECT orderNumber, status, 
	CASE 
		WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END AS details
FROM orders;