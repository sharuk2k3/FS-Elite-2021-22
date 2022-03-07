/*
Write an SQL query to display the employee number and name of employee/s working 
as CLERK and earning highest salary among CLERKS.

Note: Table name "emp".

Sample Output:
-------------
empno   ename                                                                                                           
7934    FORD

*/

select emp.empno, emp.ename from emp where emp.job = 'clerk' order by sal desc limit 1;