/*
Write an SQL query to list all the details of employees who joined before 1996.

Note:
Table name is "emp"

Sample Output:
-------------
empno   ename   job         mgr     hiredate        sal       comm    deptno                                                  
7369    SMITH   CLERK       7902    1993-06-13      800.00    0.00    20                                                      
7844    KEVIN   SALESMAN    7698    1995-06-04      1500.00   0.00    30

*/
select * from emp where hiredate < '1996-01-01';