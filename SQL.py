#Question 1: Basics of SQL Write a SQL query to retrieve all columns from the "Employees" table.	
#เลือกข้อมูลทั้งหมดจากตาราง Employee
SELECT * FROM Employee; 

#Question 2: Filtering and Sorting Retrieve the names and salaries of all employees who have a salary
#greater than $50,000, ordered by salary in descending order."
#หาชื่อผู้ที่มีเงินเดือนมากกว่า 50,000 จากตาราง Employee โดยเรียงเงินเดือนจากมากไปน้อย
SELECT Name, Salary
FROM Employee
WHERE Salary > 50000 
ORDER BY Salary DESC;

#Question 3: Aggregation Calculate the total sales amount for each product category from the "Sales" table.
#หายอดขายรวมของตาราง Sales โดยใช้ product category 
SELECT p.[Product category] AS ProductCategory, SUM(s.[Sales Amount]) AS TotalSalesAmount
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product category]; 

#Question 4: Joins Write a query to display the names of customers and the products they have purchased from the "Customers" and "Orders" tables.
#รวมตาราง Customer และ Order เข้าด้วยกัน โดยให้มี ชื่อลูกค้า (Customer) และ ตัวสินค้าที่ลูกค้าซื้อปรากฏ (Product)
SELECT c.Name AS CustomerName, p.[Product name] AS PurchasedProduct 
FROM Customer c
JOIN [Order] o ON c.[Customer ID] = o.[Customer ID]
JOIN Sales s ON o.[Order ID] = s.[Order ID]
JOIN Products p ON s.[Product ID] = p.[Product ID];

#Question 5: Subqueries List the employees who have a salary greater than the average salary of all employees.
#เลือกข้อมูลจาก Name, Salary จากตาราง Employee โดยที่ Salary มากกว่าค่าเฉลี่ยของตาราง Employee
SELECT Name, Salary 
FROM Employee
WHERE Salary > (SELECT AVG(Salary) FROM Employee);

#Question 6: Grouping and Having Find the departments with more than 5 employees and display the department name along with the count of employees.
#การจัดกลุ่มและค้นหาแผนกที่มีพนักงานตั้งแต่ 5 คนขึ้นไป และแสดงชื่อแผนกพร้อมจำนวนพนักงาน
SELECT Department, COUNT(*) AS EmployeeCount
FROM Employee
GROUP BY Department 
HAVING COUNT(*) > 5;

#Question 7: Data Modification Update the salary of an employee with ID 101 to $60,000.
#ปรับเปลี่ยนข้อมูลเงินเดือนของพนักงาน ID 101  เป็น 60,000
 
#Option 1 > database structure > Employee table >
#เพิ่ม Employee ID ก่อนใส่ข้อมูลเพิ่ม
#Modify table > Add > EmployeeID
Insert INTO Employee (EmployeeID,Salary)
VALUES (101,60000);
#Option 2
#ถ้ามีแถว Employee ID แล้ว ให้ Update
UPDATE Employee
SET Salary = 60000
WHERE EmployeeID = 101; 

#Question 8: Indexing and Optimization Suggest ways to improve the performance of a slow-performing SQL query.
#ให้ใส่เงื่อนไขเพิ่มกรณีที่ SQL ทำงานได้ช้า
#Add indexes to columns used in WHERE, JOIN, and ORDER BY clauses.

#Question 9: Data Transformation Given a table "Orders" with columns (order_id, order_date, customer_id), transform this data into a new table "MonthlyOrderSummary" with columns (year, month, total_orders, total_customers), summarizing the number of orders and unique customers per month.

CREATE TABLE IF NOT EXISTS MonthlyOrderSummary 
(  
    year INT,
    month INT,
    total_orders INT,
    total_customers INT
);

INSERT INTO MonthlyOrderSummary (year, month, total_orders, total_customers)
SELECT 
Year [Order Date] AS year, Month [Order Date] AS month, 
COUNT[Order ID] AS total_orders, COUNT(DISTINCT[Customer ID]) AS total_customers
FROM Order
GROUP BY YEAR [Order Date],MONTH [Order Date];






