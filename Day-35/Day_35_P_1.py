'''

Few people are living in a township of size N*N, where each 1*1 part 
of the township is either a villa or a swimming pool. 
You are given the structure of township as a 2d matrix of size N*N, 
filled with 0's and 1's, where '0'-indicates a swimming pool and 
'1'- indiactes a villa. 

Your task is to find a swimming pool, such that its distance to 
the nearest villa(s) is maximized, and return the distance.

If the township contains only the villas or only swimming pools, print '-1'. 

The distance used in this problem is the Manhattan distance: 
the distance between two cells (a0, b0) and (a1, b1) is |a0 - a1| + |b0 - b1|


Input Format:
-------------
Line-1: An integer N, size of the 2d matrix.
Next N lines: N space separated integers, matrix[][] either 0 or 1.

Output Format:
--------------
An integer, maximum distance.


Sample Input-1:
---------------
4
1 0 1 1
0 0 0 0
1 0 1 0
1 0 0 1

Sample Output-1:
----------------
2

Explanation: 
------------
The swimming pool at (1, 1) is with distance 2 from the nearest villas.


Sample Input-2:
---------------
4
1 0 0 0
0 0 0 0
1 0 0 0
0 1 0 1

Sample Output-2:
----------------
3

Explanation: 
------------
The swimming pool at (0,3) or (1, 2) are with distance 3 from the nearest villas.


'''

#Solution 9/10

def Solution(matrix):
    n = len(matrix)
    if n == 0:
        return -1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = float('inf')
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else:
                if i-1 >= 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i-1][j]+1)
                if j-1 >= 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j-1]+1)
                if i+1 < n:
                    matrix[i][j] = min(matrix[i][j], matrix[i+1][j]+1)
                if j+1 < n:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j+1]+1)
    max_dist = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > max_dist:
                max_dist = matrix[i][j]
    if max_dist == float('inf'):
        return -1
    return max_dist
    
if __name__=="__main__":
    n=int(input())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    print(Solution(matrix))

'''
#CPP SOl

#include<bits/stdc++.h>
using namespace std;


int main(){
    
    int n;
    cin>>n;
    
    vector<vector<int>> temp(n+1,vector<int>(n+1,0));
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>temp[i][j];
        }
    }
    vector<vector<int>> visited(n+1,vector<int>(n+1,0));
    queue<pair<int,int>> q;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
             if(temp[i][j]==1){
                 q.push({i,j});
                 visited[i][j]=1;
             }
            
        }
    }
    if(q.size()==0 || q.size()==n*n){
        cout<<-1<<endl;
        return 0;
    }
    int x[] = {-1,1,0,0};
    int y[] = {0,0,-1,1};
    int ans=0;
    while(!q.empty()){
        int size = q.size();
        int flag=1;
        //cout<<1+ans<<endl;
        for(int j=0;j<size;j++){
            pair<int,int> p= q.front();
            //cout<<p.first<<" "<<p.second<<endl;
            q.pop();
            
            int l,r;
            l=p.first;
            r=p.second;
            for(int i=0;i<4;i++){
                if(l+x[i]>=1 && l+x[i]<=n && r+y[i]>=1 && r+y[i]<=n && !visited[l+x[i]][r+y[i]]){
                    q.push({l+x[i],r+y[i]});
                    visited[l+x[i]][r+y[i]]=1;
                    flag=0;
                }
                
            }
            
            
            
            
        }
        if(!flag){
            ans++;
        }
        
    }
    cout<<ans<<endl;
    
    
    
}

'''