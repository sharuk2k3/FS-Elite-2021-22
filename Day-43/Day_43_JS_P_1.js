/*
Write a JS program to count the number of valid mobile numbers in the 
given employee data with following constraint:
	- Mobile number should start with 7 or 8 or 9 only

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
print an integer value                                                                                                             

*/

// Input JSON file.
const empdata= require('./empInfo.json');

//Implement Your Code Here

let ans = 0;
for(let emp of empdata) {
    if(/^[7,8,9]\d{9}$/.test(emp.phone)) {
        ans += 1;
    }
}
console.log(ans);