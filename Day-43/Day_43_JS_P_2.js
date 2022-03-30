/*
Write a JS program to find the number of employees working in each college,
the college name is extracted from email as follows:
    - For given email: sudhakar@kmit.in, the college name is "kmit".

Sample Document
---------------

{
    "id": 1,
    "name": "nagireddy",
    "email": "avnreddy@kmit.com",
    "phone": "9876543210"
}


Sample Output:
--------------
kmit => 4                                                                                                               
ngit => 3                                                                                                               
kmec => 3                                                                                                               

*/

// Input JSON file.
const empdata= require('./empInfo.json');

var map = {};
//Implement Your Code Here
for(let emp of empdata) {
    let s = emp.email.split("@")[1];
    s = s.split(".")[0];
    if(s in map) {
        map[s] += 1;
    } else {
        map[s] = 1;
    }
}

for(var i in map) {
    console.log(i + " => " + map[i]);
}