/*
'''


Mohan is given a task to decorate a wall with balloons.
He is given an unlimited set of ballons of three different colors.

The decoration should have N rows of 3 balloons each. 
He has to make sure that no two adjacent balloons have the same colour.
both vertically and horizontally.

Your task is to help Mr Mohan to find the number of ways to decorate the wall,  
the answer must be computed modulo 10^9 + 7

Input Format:
-------------
An integer N

Output Format:
--------------
Print an integer as outpur, number of ways to decorate.


Sample Input-1:
---------------
1

Sample Output-1:
----------------
12

Explanation:
------------
Suppose the colors are, B-Blue, W-White, R-Red. Given N is 1
RBR	BRB	WRB
RBW	BRW	WRW
RWR	BWR	WBR
RWB	BWB	WBW


Sample Input-2:
---------------
2

Sample Output-2:
----------------
54


'''

#Solution:

*/
#include<bits/stdc++.h>
using namespace std;

int mod = 1e9+7;
int numOfWays(int n) {
    vector<long long int> v2(n,0); vector<long long int> v1(n,0);
    v2[0] = 6; v1[0] = 6;
    for(long long int i = 1; i<n;i++)
    {
        v1[i] = ((2*v2[i-1])%mod + (v1[i-1] * 3)%mod )%mod;
        v2[i] = ((2*v2[i-1])%mod + (v1[i-1] * 2)%mod )%mod;
            
    }
    return (int)((v2[n-1]%mod + v1[n-1]%mod)%mod);
}

int main(){
    
    
    int n;
    cin>>n;
    
    cout<<numOfWays(n)<<endl;
    
    
    
}
