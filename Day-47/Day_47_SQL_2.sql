/* 
Write an SQL query to display allthe details of employee(s) who are in 
sales department and grade is 3.

Sample Output:
-------------
empno   ename   job         mgr     hiredate    sal      comm    deptno                                                  
7844    KEVIN   SALESMAN    7698    1995-06-04  1500.00  0.00    30

*/

select * from emp where deptno=30 and grade=3;