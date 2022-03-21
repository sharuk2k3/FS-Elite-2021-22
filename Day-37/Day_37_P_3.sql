/*
Write an SQL query to Display the department name(s), where the dept name is 
equal to 'no of employees - 2' in any other department.

Sample Output:
-------------
dname                                                                                                                   
Research                                                                                                                

*/

select dname from dept d where length(dname)+2 in (select count(*) from emp e where e.deptno<>d.deptno group by deptno);