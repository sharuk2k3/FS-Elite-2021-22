/*
Using Map Filter Reduce function complete the following task:

    - MAP FUNCTION:
        Here the data is manipulated or updated based on below conditions,
        Condition#1: if sal>50k then 15 percent hike in sal.
        Condition#2: if sal>30k and <=50 then 20 percent hike in sal.
        Condition#3: if sal<=30 then 25 percent hike in sal.
    
    - FILTER FUNCTION: 
        Retains the employee data whose sal<=50
    
    - REDUCE FUNCTION:
        Finds the highest salary(scalar value) from the filtered employee data.

Sample Input
------------
6      -----> Number of employees
aa 10  -----> (empName  salary)
bb 50
cc 35
dd 12
ww 60
ll 9

Sample Output
-------------
42      ------> highest salary (of filtered emp data)

*/

var n=null;

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('', function(input){
    n = parseInt(input);
});

var i=0;
var empList=[];
readline.on('line',function(line){
  var data=line.split(' ');
  item={};
  item["empName"] = data[0];
  item["sal"] = parseInt(data[1]);
  empList.push(item);
  i++;
  if(i==n){
      readline.close();
      mrf(empList);
  }
});
  
 
function mrf(empList){
    //Implemet your code here

    const arr = empList.map(emp => {
        if(emp.sal > 50) {
            return (emp.sal + emp.sal*0.15);
        } else if(emp.sal > 30) {
            return (emp.sal + emp.sal*0.20);
        } else {
            return (emp.sal + emp.sal*0.25);
        }
    });
    
    const arr2 = arr.filter((sal) => {
        return sal<=50;
    });
    
    const ans = arr2.reduce((p, c) => {
        if(p<c) {
            p = c
        }
        return p
    });
    
    console.log(ans);
}