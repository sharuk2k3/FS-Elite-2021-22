/*'''

You are playing a shooting game.
There are N bottles hanging to a rod, i-th bottle numbered bottle[i].

If you shoot i-th bottle, you will get bottle[i-1]*bottle[i]*bottle[i+1] points.
The more points you score, the more rewards you can win.

Your task is to score the maximum points by shooting all the ballons wisely.

Note: After you shoot bottle at i-th index, bottles at i-1 and i+1 positions
become adjacent. if there is no existing 'i-1' or 'i+1' positions for selected bottle.
you can assume that bottle[i-1] = bottle[i+1] = 1.

Input Format:
-------------
N space separated integers bottles[].

Output Format:
--------------
Print an integer, maximum points you can get.


Sample Input:
---------------
3 1 5 8

Sample Output:
----------------
167

Explanation:
------------
Given bottles = [3, 1, 5, 8] 
position 	points
--------------------
1				3*1*5
5				3*5*8
3				1*3*8
8				1*8*1
--------------------
Total = 167


Sample Input:
---------------
2 1 3 5 4

Sample Output:
----------------
102

Explanation:
------------
Given bottles = [2, 1, 3, 5, 4] 

position 	points
--------------------
5				3*5*4
1				2*1*3
3				2*3*4
2				1*2*4
4				1*4*1
--------------------
Total = 102


'''

#Solution:
*/

#include<bits/stdc++.h>
using namespace std;

int rep(int i,int j,int n,vector<int>& temp,vector<vector<int>>& dp){
    
    if(i>j){
        return 0;
    }
    if(i==j){
        int ans=temp[i];
        if(i-1>=0){
            ans=ans*temp[i-1];
        }
        if(i+1<n){
            ans=ans*temp[i+1];
        }
        return ans;
    }
    if(dp[i][j]!=-1){
        return dp[i][j];
    }
    int ans=INT_MIN;
    for(int k=i;k<=j;k++){
        ans=max(ans,temp[k]*temp[i-1]*temp[j+1]+rep(i,k-1,n,temp,dp)+rep(k+1,j,n,temp,dp));
        
    }
    return dp[i][j]=ans;
    
    
}

int main(){
    
    vector<int> temp;
    string s;
    getline(cin,s);
    
    temp.push_back(1);
    
    stringstream ss(s);
    int x;
    while(ss>>x){
        temp.push_back(x);
    }
    
    temp.push_back(1);
    int n = temp.size();
    
    vector<vector<int>> dp(n+2,vector<int>(n+2,-1));
    cout<<rep(1,n-2,n,temp,dp)<<endl;
}