/*
Write a javascript program to find the unique domain names,
from the given list of email-id's.


Sample Input:
-------------
abc@kmit.in def@gmail.com kfs@kmit.in hello@gmail.com funnyy@yahoo.com                                                  

Sample Output:
--------------                                                  
kmit.in                                                                                                                 
gmail.com                                                                                                               
yahoo.com                                                                        

*/

var readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

var emails=[];

let uniqueDomainSet=new Set();

readline.on('line',function(line){
  emails=line.split(' ');
   uniqueDomains(emails);
});

function uniqueDomains(data){
    //implement you are code here.
    for(let i=0;i<data.length;i++){
        let domain=data[i].split('@');
        uniqueDomainSet.add(domain[1]);
    }
    console.log(uniqueDomainSet);
}
