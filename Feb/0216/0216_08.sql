SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM customers;
-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (SELECT(AVG(MSRP)) FROM products)
ORDER BY MSRP;

-- 문제 2
SELECT customers.customerNumber, customers.customerName
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderDate BETWEEN '2003-01-06' AND '2003-3-26'
ORDER BY customerNumber;

-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM products
WHERE productLine = 'Classic Cars'
ORDER BY MSRP DESC
LIMIT 1;

-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
  SELECT country
  FROM customers
  GROUP BY country
  ORDER BY COUNT(*) DESC
  LIMIT 1
)
ORDER BY customerNumber;

-- 문제 5
SELECT customers.customerNumber, customers.customerName, COUNT(*) AS order_count
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
GROUP BY customers.customerNumber
ORDER BY order_count DESC
LIMIT 1;

-- 문제 6
SELECT DISTINCT products.productCode, products.productName
FROM orders
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
JOIN products ON orderdetails.productCode = products.productCode
WHERE orders.orderDate BETWEEN '2004-01-01' AND '2004-12-31'
ORDER BY products.productCODE DESC;