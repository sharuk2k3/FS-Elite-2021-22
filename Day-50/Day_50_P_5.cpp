/*
'''

Mr Sudhakar has a set of N dices, the dice has different faces of 
movie characters. The possibility score of i-th dice to show the JOKER face
when it is rolled is given as pScore[i].

Your task is to help Mr Sudhakar to find and return the possibility score, that
the number of dices showing JOKER face equals to value F, 
when you roll all N dices only once.

NOTE:
-----
Your output will be accepted as correct,
if they are within 10^-5 of the correct output.

Input Format:
-------------
Line-1: An integer N, number of chances.
Line-2: N space separated double values, possibility pScore[]
Line-3: An integer F, number of dices to show JOKER face up.   

Output Format:
--------------
Print a double result, the possibility score.


Sample Input-1:
---------------
4
0.5 0.25 0.75 0.5
2

Sample Output-1:
----------------
0.40625



Sample Input-2:
---------------
1
0.6
1

Sample Output-2:
----------------
0.60000


Sample Input-3:
---------------
3
0.4 0.5 0.6
0

Sample Output-3:
----------------
0.12000



'''

*/
#include<bits/stdc++.h>
    using namespace std;
     
     vector<double> arr;
     vector<vector<double>> dp;
     
     double get(int i, int j){
         if(i==arr.size() && j==0) return (double) 1;
         if(j<0 || i==arr.size()) return (double) 0;
        
        if(dp[i][j]!= (double) -1) return dp[i][j];
        
        double x = arr[i]*get(i+1,j-1);
        double y = (1-arr[i])*get(i+1,j);
        return dp[i][j] = x+y;
    }
    
    int main()
    {
        int n,j;
        cin>>n;
        arr.resize(n);
        
        for(double &i:arr) 
            cin>>i;
        cin>>j;
        
        dp.resize(n+1,vector<double>(j+1,-1));
        
        // cout
        printf("%.5f",get(0,j));
        
        return 0;
    }