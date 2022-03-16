/* 
Write an SQL query to list the employee names starting with ‘S’ and 
ending with ‘H’ and having a length of 5 chars.

Sample Output:
-------------
ename                                                                                                                   
SMITH

*/

select ename from emp where ename like 'S%' and ename like '%H' and length(ename) = 5;