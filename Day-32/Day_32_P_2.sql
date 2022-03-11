/* 
Write an SQL query to display unique enames, dname, location of employee 
( join ‘emp’ and ‘dept’ tables) where employee name starts with 'A'?

Sample Output:
-------------
ename   dname       location                                                                                                
ALLEN   Accounting  New York                                                                                        
ALLEN   Sales       Chicago 

*/

select ename, dname, location from emp e join dept d on e.deptno=d.deptno where ename like 'A%';