/*
Write an SQL query to display the unique names of employees who are working in the 
company for the past 25 years.

Note: Table name "emp"

Sample Output:
-------------
ename                                                                                                                   
SMITH                                                                                                                   
ALLEN                                                                                                                   
JONES                                                                                                                   
BLAKE                                                                                                                   
CLARK                                                                                                                   
SCOTT                                                                                                                   
KEVIN                                                                                                                   

*/


select ename from emp where hiredate between '1980-01-01' and '1996-01-01';