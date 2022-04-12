/*
'''

There are n boxes of balls in a row, every i-th box contains balls[i] balls.

A series of boxes is called Special, if it consists of at least 
three boxes and iff the difference between the number of balls in any 
two consecutive boxes is same.

A subset of boxes is called Special Subset,
if subset[i], subset[i+1], subset[i+2], ..., subset[j] is Special.

Your task is to findout the number of Special Subsets in the row of boxes.

Input Format:
-------------
Line-1 : An integer N, number of boxes.
Line-2 : N space separated integers balls[i], i-th box contains balls[i] balls. 

Output Format:
--------------
Print an integer, number of Special Subsets.


Sample Input:
---------------
4
1 2 3 4

Sample Output:
----------------
3

Explanation:
------------
Special Subsets are: 
[1,2,3], [2,3,4], [1,2,3,4].


Sample Input:
---------------
5
1 3 5 7 9

Sample Output:
----------------
6


Explanation:
------------
Special Subsets are: 
[1,3,5], [3,5,7], [5,7,9], [1,3,5,7], [3,5,7,9], [1,3,5,7,9].



'''

#Solution:
*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cin>>n;
    
    vector<int> temp(n);
    for(int i=0;i<n;i++){
        cin>>temp[i];
    }
    
    int ans=0;
    int start=-1;
    for(int i=2;i<n;i++){
        if(temp[i]-temp[i-1]==temp[i-1]-temp[i-2]){
            if(start==-1){
                start=i-2;
                ans++;
            }
            else{
                ans+=(i-start-1);
            }
            
        }
        else{
            start=-1;
        }
        
    }
    cout<<ans<<endl;
    
    
}