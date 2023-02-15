SELECT * FROM products;
SELECT * FROM orderdetails;
SELECT * FROM orders;

-- 문제 1
SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices ON employees.officeCode = offices.officeCode
ORDER BY employeeNumber;

-- 문제 2
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 3
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 4
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 5
-- 문제 2는 교집합을 포함한 왼쪽 테이블 전체, 3은 교집합을 포함한 오른쪽 테이블 전체, 4번은 교집합 부분을 표시하여 보여준다.
-- 표시되는 영역의 기준이 다르다.

-- 문제 6
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT OUTER JOIN offices ON customers.city = offices.city
UNION
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT OUTER JOIN offices ON customers.city = offices.city
WHERE customers.city IS NULL
ORDER BY customerNumber DESC;

-- 문제 7
SELECT orders.orderNumber, orderDate
FROM orderdetails
INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber
ORDER by orderNumber;

-- 문제 8
SELECT orderNumber, products.productCode, productName
FROM orderdetails
INNER JOIN products ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

SHOW COLUMNS FROM orderdetails;
SHOW COLUMNS FROM orders;
SHOW COLUMNS FROM products;
-- 문제 9
SELECT orderdetails.orderNumber, orderdetails.productCode, orderDate, productName
FROM orderdetails
INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;