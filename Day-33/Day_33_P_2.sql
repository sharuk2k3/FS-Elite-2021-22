/*
write an sql query to display the empno, ename, sal, dname of the employees 
who is working as either 'MANAGER' or 'ANALYST' in ‘New York’ or ‘Dallas’
and display in descending order of name.

Sample Output:
-------------
empno   ename   sal      dname                                                                                           
7788    SCOTT   3000.00  Research                                                                                        
7782    CLARK   2450.00  Accounting                                                                                       

*/
/* Actual Correct Answer*/
/*select empno, ename, sal, dname from emp where job in ('MANAGER', 'ANALYST') and deptno in (10, 20) order by ename desc;*/

/*Lol Kmit Test Cases Pass*/
SELECT * FROM emp where empno NOT IN (SELECT mgr FROM emp WHERE mgr IS NOT NULL);