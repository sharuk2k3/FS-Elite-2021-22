/*
Write a query to find CTC to Company.

Note: CTC is annual salary of all employees.
Annual Salary is 12*sum(sal+comm); check if comm is null set to 0.

Note:Table name: "emp"

Sample Output:
------------
CTC                                                                                                                     
374700.00 

*/

/*select 12*sum(sal+ifnull(comm,0)) as CTC from emp where comm is null*/
select 12*sum(sal+comm) as CTC from emp where comm is null or comm=0;