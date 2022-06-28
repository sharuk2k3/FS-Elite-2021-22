/* 
Write an SQL query to list the empno,ename,annual_sal,daily_sal of all 
the salesmen in the ascending order of their annual_sal

Sample Output:
-------------
empno   ename   annual_sal      daily_sal                                                                               
7521    ALLEN   15000.00        41.095890                                                                               
7654    MARTIN  15000.00        41.095890

*/
select empno, ename, (sal*12) as annual_sal, ((sal*12)/365) as daily_sal from emp where job="SALESMAN" order by annual_sal;
