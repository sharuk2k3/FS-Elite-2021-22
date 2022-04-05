/*

Bharath is given a set of integers arr[] of length N.
He planned split arr[] into four subsets.

He also defined a rule set to split the set arr[] as follows:
	- select three indices p, q, r, where p < q < r.
	- split the arr[] as four subsets: sub(0, p-1), sub(p+1, q-1) sub(q+1, r-1), sub(r+1, N-1)
	- the sum of elements in each subset should be equal .
	  i.e., subsum(0, p-1) = subsum(p+1, q-1) = subsum(q+1, r-1) = subsum(r+1, N-1)

Your task is to help Bharath to split the set arr[] with the above rules,
If you are able to satisfy all the rules , return true. Otherwise, false.


Input Format:
-------------
Line-1 -> An integer N, number of array elements
Line-2 -> N space separated integers, elements of the array.

Output Format:
--------------
Print an boolean result.


Sample Input-1:
---------------
10
2 6 1 7 2 7 8 7 7 0

Sample Output-1:
----------------
false


Sample Input-2:
---------------
10
3 3 4 1 5 4 2 4 5 6

Sample Output-2:
----------------
true

Explanation:
--------------
p = 2, q = 5, r = 8.
subsum(0, i - 1) = subsum(0, 1) = 6
subsum(i + 1, j - 1) = subsum(3, 4) = 6
subsum(j + 1, k - 1) = subsum(6, 7) = 6
subsum(k + 1, n - 1) = subsum(9) = 6


*/

//SOLUTION

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cin>>n;
    
    vector<int> temp(n);
    for(int i=0;i<n;i++){
        cin>>temp[i];
    }
    
    vector<int> prefix(n+2,0);
    prefix[0]=temp[0];
    
    for(int i=1;i<n;i++){
        prefix[i]=prefix[i-1]+temp[i];
    }
    
    int ans=0;
    for(int i=1;i<n;i++){
        for(int j=i+2;j<n;j++){
            for(int k=j+2;k<n-1;k++){
                if(prefix[i-1]==prefix[j-1]-prefix[i] && prefix[i-1]==prefix[k-1]-prefix[j] && prefix[n-1]-prefix[k]==prefix[i-1]){
                    ans=1;
                }
            }
        }
    }
    
    if(ans){
        cout<<"true"<<endl;
    }
    else{
        cout<<"false"<<endl;
    }
    
    
}