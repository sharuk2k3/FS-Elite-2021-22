/*
Write an SQL query to display the names of employees from department number 10 
with salary greater than that of any employee working in other departments.

Sample Output:
-------------
ename   sal       deptno                                                                                                  
ALLEN   1600.00   10                                                                                                      

*/
SELECT ename,sal,deptno FROM emp WHERE sal=(SELECT MAX(sal) FROM emp);
