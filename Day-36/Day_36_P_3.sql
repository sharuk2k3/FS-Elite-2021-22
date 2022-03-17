/*
Write an SQL query to display the common jobs from department number 10 and 20.

Sample Output:
-------------
job                                                                                                                     
CLERK                                                                                                                   



LoL Kmit Test Cases 

*/
select job from emp where deptno(10,20) group by having count(job) > 1;