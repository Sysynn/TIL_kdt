-- 문제 1
SELECT * FROM employees;

-- 문제 2
SELECT customerNumber, customerName, phone FROM customers;

-- 문제 3
SELECT firstName, lastName, email FROM employees ORDER BY firstName;

-- 문제 4
SELECT firstName AS '이름', lastName AS '성', email AS '이메일' FROM employees ORDER BY firstName;

-- 문제 5
SELECT employeeNumber, lastName, firstName, officeCode, jobTitle FROM employees ORDER BY jobTitle DESC, officeCode DESC;

-- 문제 6
SELECT * FROM orderdetails ORDER BY quantityOrdered, priceEach;

-- 문제 7
SELECT customerNumber, country, contactFirstName FROM customers ORDER BY country, contactFirstName DESC;

-- 문제 8
SELECT productCode, quantityInStock, buyPrice, quantityInStock * buyPrice FROM products ORDER BY quantityInStock * buyPrice DESC;

SELECT DISTINCT lastName FROM employees ORDER BY lastName ASC;

SELECT lastName, firstName, officeCode FROM employees WHERE officeCode = 1;
SELECT lastName, firstName, jobTitle FROM employees WHERE jobTitle != "Sales Rep";
SELECT lastName, firstName, officeCode, jobTitle FROM employees WHERE officeCode >= 3 AND jobTitle = "Sales Rep";
SELECT lastName, firstName, officeCode, jobTitle FROM employees WHERE officeCode < 5 AND jobTitle != "Sales Rep";
SELECT lastName, firstName, officeCode FROM employees WHERE officeCode >= 1 AND officeCode <= 4;
SELECT lastName, firstName, officeCode FROM employees WHERE officeCode BETWEEN 1 AND 4;
SELECT lastName, firstName, officeCode FROM employees WHERE officeCode IN (1, 3, 4);
SELECT lastName, firstName FROM employees WHERE lastName LIKE "%son";
SELECT lastName, firstName FROM employees WHERE firstName LIKE "___y";
SELECT firstName, officeCode FROM employees ORDER BY officeCode DESC LIMIT 3, 5;
SELECT jobTitle, COUNT(*) FROM employees GROUP BY jobTitle;
SELECT country, AVG(creditLimit) AS averageOfCreditLimit FROM customers GROUP BY country ORDER BY AVG(creditLimit) DESC;
SELECT postalCode FROM customers WHERE postalCode IS NOT NULL ORDER BY postalCode;