/*
Write an SQL query to display the names of departments, in which atleast 
3 employees are working in that department.

Sample Output:
-------------
dname           count(*)                                                                                                        
Accounting        3                                                                                                       
Research          6                                                                                                       
Sales             3 

*/
select d.dname, count(*) from emp e, dept d where e.deptno=d.deptno group by d.dname having count(*)>=3;