/*
Write an SQL query to display all the details of employees 
who are not working as managers.

Sample Output:
-------------
empno   ename   job         mgr     hiredate        sal         comm    deptno                                                  
7369    SMITH   CLERK       7902    1993-06-13      800.00      0.00    20                                                      
7934    FORD    CLERK       7782    2000-01-21      1300.00     NULL    10  

*/

select * from emp where job != 'MGR';