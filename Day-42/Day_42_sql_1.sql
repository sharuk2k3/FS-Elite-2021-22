/*
Write an SQL query to display the manager name(s) and count of employees 
working under that manager, who is having maximum number of employeess 
among all the managers.

Sample Output:
-------------
ename   count                                                                                                           
BLAKE   5                                                                                                               

*/

select ename, count(*) as count from (select distinct e.ename, m.ename as mname 
from employee e, manager m where e.mgr = m.eid) as t group by ename order by count desc limit 1;