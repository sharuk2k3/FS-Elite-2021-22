/*
Write an SQL query to display the names of the salesman who earns a salary 
more than the highest salary of any clerk.

Sample Output:
-------------
ename                                                                                                                   
ALLEN                                                                                                                   

*/
select ename from emp
where job = 'SALESMAN' and sal > (select max(sal) from emp where job = 'CLERK');