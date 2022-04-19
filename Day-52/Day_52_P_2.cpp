/*'''

Due to COVID-19 impact, to attract people to watch the movies in theatre,
One of the Theatre management introduced a scheme 
to give mobiles for Lucky winners after the show.

The theatre has M rows and N seats in each row.
The seats are numbered in a strange order (No duplicates).

You need to find out the Lucky Winners  in such way that, the seat number 
of the person should be the minimum in its row and maximum in its column.

You have to return all seat numbers of lucky winners .

Input Format:
-------------
Line-1 -> Two integers M and N
Next M lines -> N space separated integers, seat numbers.

Output Format:
--------------
Print the list of seat numbers of Lucky Winners.


Sample Input-1:
---------------
3 3
3 7 8
9 11 13
15 16 17

Sample Output-1:
----------------
15


Sample Input-2:
---------------
3 4
1 10 4 2
9 3 8 7
15 16 17 12

Sample Output-2:
----------------
12


'''


#Solution:
*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n,m;
    cin>>n>>m;
    
    vector<vector<int>> temp(n+3,vector<int>(m+3));
    for(int i=1;i<=n;i++){
        int ans=INT_MAX;
        for(int j=1;j<=m;j++){
            cin>>temp[i][j];
            ans=min(ans,temp[i][j]);
        }
        temp[i][m+1]=ans;
    }
    
    for(int i=1;i<=m;i++){
        int ans = INT_MIN;
        for(int j=1;j<=n;j++){
            ans=max(ans,temp[j][i]);
        }
        temp[n+1][i]=ans;
    }
    vector<int> ret;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(temp[i][j]==temp[i][m+1] && temp[i][j]==temp[n+1][j]){
                ret.push_back(temp[i][j]);
            }
        }
    }
    
    for(auto x: ret){
        cout<<x<<" ";
    }
    cout<<endl;
}