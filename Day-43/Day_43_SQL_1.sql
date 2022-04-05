/*
Write an SQL query to print the department number, employee name,salary ,job,
and Net Salary(Salary+Commission) of the employee(s), who earns the second 
highest net salary.

Sample Output:
-------------
deptno   ename    sal       job         Net Salary                                                                              
40       MARTIN   1250.00   SALESMAN    2650.00 

*/

select deptno, ename, sal, job, sal + comm as net_salary from emp where sal + comm = (select max(sal + comm) from emp) and sal + comm < (select max(sal + comm) from emp);


