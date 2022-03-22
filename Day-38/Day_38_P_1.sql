/*
Write an SQL query to list out(ename,mgr,and sal) the lowest paid employees 
working for each manager,exclude any employee whose salary is less than 1000 
sort the output by salary.

Sample Output:
-------------
ename   mgr     sal                                                                                                     
FORD    7782    1300.00                                                                                                 
SCOTT   7566    3000.00                                                                                                 

*/

select ename,mgr,sal from emp where sal<>1000 order by sal;