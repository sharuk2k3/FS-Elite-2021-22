/*
Write an SQL query to find the all the details of the employees who earn the
same salary as the minimum salary for all departments by ascending order

Sample Output:
-------------
empno   ename   job       mgr     hiredate        sal      comm     deptno                                                  
7369    SMITH   CLERK     7902    1993-06-13      800.00   0.00     20                                                      
7521    ALLEN   SALESMAN  7698    1996-03-26      1250.00  500.00   30                                              
7839    KEVIN   PRESIDENT NULL    1990-06-09      5000.00  0.00     40

*/

select e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm, e.deptno from employee e, (select min(sal) as min_sal from employee) as t where e.sal = t.min_sal;
