/*
Write an SQL query to display the unique names of employees who are working as clerk, 
salesman or analyst and drawing a salary more than 1000.

Note: Table names "emp","dept".

Sample Output:
-------------
ename                                                                                                                   
ALLEN                                                                                                                   
MARTIN                                                                                                                  
KEVIN                                                                                                                   


*/

select distinct ename from emp where job in ('clerk','salesman','analyst') and sal > 1000;