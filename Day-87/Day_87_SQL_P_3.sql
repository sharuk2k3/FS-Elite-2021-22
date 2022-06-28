/* 
Write an SQL query to list the ename and salary of the 5th highest paid employee

Sample Output:
-------------
ename   sal                                                                                                             
CLARK   2450.00

*/

select ename,sal from emp order by sal DESC limit 5,1;