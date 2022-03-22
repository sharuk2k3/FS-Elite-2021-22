/*
Write an SQL query to display the name of department where highest number of 
employees are working.

Sample Output:
-------------
dname                                                                                                                   
Research

*/

select dname from dept where dno in (select dno from emp group by dno having count(*)= (select max(count(dno)) from emp group by dno));