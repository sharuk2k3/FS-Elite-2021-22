/*
Write an SQl query to display the department number, minimum salary, 
maximum salary of each department.

Sample Output:
--------------
deptno  min_salary  max_salary                                                                                      
10      1300.00     2450.00 

*/

select deptno, sum(salary) as min_salary, max(salary) as max_salary from emp group by deptno;