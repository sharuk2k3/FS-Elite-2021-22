/*
Write an SQL query to display the name, job, salary of the employees in the 
department with the highest average salary among all the departments.

Sample Output:
-------------
ename   job     sal                                                                                                     
MARTIN  SALESMAN        1250.00  

*/
select ename,job,sal from emp where job='SALESMAN' and sal=(select avg(sal) from emp where job='SALESMAN');
