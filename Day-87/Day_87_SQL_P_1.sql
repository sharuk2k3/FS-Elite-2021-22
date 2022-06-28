/* 
Write an SQL query to list the empno,ename,hiredate,curr_date  & exp in 
the ascending order of the exp [Experience in years].

Sample Output:
-------------
empno   ename   hiredate        curr_date       exp                                                                     
7900    JAMES   2000-06-23      2022-06-22      21                                                                      
7934    FORD    2000-01-21      2022-06-22      22 

*/


select empno,ename,hiredate,curdate() as curr_date,
(floor(datediff(curdate(),hiredate)/365)) as exp from emp order by exp;