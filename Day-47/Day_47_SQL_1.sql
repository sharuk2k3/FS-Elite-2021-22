/*
Write an SQL query to display the employee number and name of employee working 
as CLERK and earning highest salary among CLERKS.

Sample Output:
-------------
empno   ename                                                                                                           
7934    FORD 

*/

SELECT empno,
  ename
FROM emp
WHERE job='CLERK'
AND sal  =
  (SELECT MAX(sal) FROM emp WHERE job='CLERK'
  );