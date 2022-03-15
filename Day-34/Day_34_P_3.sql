/*
Write a SQL query to display the names of the employees who earn highest salary
in their respective departments.

Sample Output:
--------------
ename   salary                                                                                                          
BLAKE   2850.00
FORD    3000.00

*/

select ename, sal as salary from emp e where sal = (select max(sal) from emp e1 where e1.deptno = e.deptno);