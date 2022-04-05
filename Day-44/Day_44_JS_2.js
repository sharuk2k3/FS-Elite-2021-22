/*
Given two lists of numbers, the length of the lists may differ,
Your target is to find the intersection of two lists, each element 
in the result must appear as many times as it shows in both 
the lists and you must return the result in the given order of lists.

Input Format:
-------------
Two space separated strings, each string contains comma separated numbers.

Output Format:
--------------
Print an array of numbers.


Sample Input-1:
---------------
2,3,3,2 3,3

Sample Output-1:
----------------
3,3,


Sample Input-2:
---------------
5,7,3 7,5,7,8,5

Sample Output-2:
----------------
5,7,

*/

let readline=require('readline').createInterface({input:process.stdin,output:process.stdout});
let n;
let arr1;
let arr2;
readline.question('',function(line){
	n=line.split(" ")
	arr1=n[0].split(",").map(i=>Number(i));
	arr2=n[1].split(",").map(j=>Number(j));
	solution(arr1,arr2);
	readline.close();
});

function solution(nums1, nums2) {
    // implement your code here
}