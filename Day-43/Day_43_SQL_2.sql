/*
Write an SQL query to display all the details those earners whose salary is 
out of the grade available in Sal grade table

Sample Output:
-------------
empno   ename   job     mgr     hiredate        sal     comm    deptno 

*/

select * from emp where sal < (select min(losal) from salgrade) or sal>(select max(hisal) from salgrade);
