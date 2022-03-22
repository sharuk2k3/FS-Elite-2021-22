/*
Write an SQL query to display all the details of managers who are not working 
under the president.

Sample Output:
-------------
empno   ename   job     mgr     hiredate        sal     comm    deptno                                                  
7902    FORD    ANALYST 7566    1997-12-05      3000.00 NULL    20 

*/

select empno,ename,job,mgr,hiredate,sal,comm,deptno from emp where job='MANAGER' and mgr not in (select empno from emp where job='PRESIDENT');