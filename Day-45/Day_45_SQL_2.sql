/*
Write a SQL query to find those employees whose salary is less than 
the salary of his/her manager but more than the salary of any other manager

Sample Output:
--------------
empno   ename   sal                                                                                                     
7566    JONES   2975.00                                                                                                 

*/
select E1.empno,E1.ename,E1.sal from emp E1,emp E2 where E1.mgr=E2.empno and E1.sal<E2.sal and E1.sal>any(select E2.sal from emp E2 where job='MANAGER');