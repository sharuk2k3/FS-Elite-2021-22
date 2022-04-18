/*
'''



Pandavas and Kauravas are ruling two different kingdoms sepertaed by river.
If you connect both the kingdoms they will be in Square shaped land.
Land occupied by the kingdoms, indiacted with 1's and the river, indiacted with 0's.

Now, Pandavas and Kauravas decided to build a bridge on the river for easy 
connectivity. As the cost of building a bridge will be high, they have decided 
to reduce the length of the bridge. You are allowed to build the bridge on 
the river cells, connected by 4 directions only (up, down,left,right).

Your task is to help the Kings, to minimize the occupation of river cells, 
to build the bridge with minimum cost. And return the count of river cells occupied.

Input Format:
-------------
Line-1: An integer N, size of the land.
Next N lines: N space separated integers, either 0 or 1. 

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
4
1 1 1 0
1 0 0 0
1 0 0 1
0 0 1 1

Sample Output-1:
----------------
2


Sample Input-2:
---------------
5
1 1 0 0 0
1 1 0 0 0
0 0 0 0 1
0 0 0 1 1
0 0 1 1 1

Sample Output-2:
----------------
3



'''
*/

#include<bits/stdc++.h>
using namespace std;

void dfs(int i,int j,vector<vector<int>>& visited,vector<vector<int>>& temp,int n){
    
    if(i<1 || i>n || j<1 || j>n || visited[i][j] || temp[i][j]==0){
        return;
    }
    visited[i][j]=1;
    dfs(i+1,j,visited,temp,n);
    dfs(i-1,j,visited,temp,n);
    dfs(i,j+1,visited,temp,n);
    dfs(i,j-1,visited,temp,n);
    
    
}

int dx[4]={-1,0,1,0};
int dy[4]= {0,-1,0,1};

int main(){
    
    int n;
    cin>>n;
    
    vector<vector<int>> temp(n+2,vector<int>(n+2,0));
    vector<vector<int>> visited(n+2,vector<int>(n+2,0));
    queue<pair<int,int>> q;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>temp[i][j];
            
        }
    }
    int flag=1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(temp[i][j]){
                dfs(i,j,visited,temp,n);
                flag=0;
                break;
            }
        }
        if(!flag){
            break;
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(temp[i][j] && visited[i][j]==0){
                q.push({i,j});
                visited[i][j]=-1;
            }
            
        }
    }
    
    
    int count=0;
    while(!q.empty()){
        count++;
        int size = q.size();
        for(int i=0;i<size;i++){
            
            int x = q.front().first;
            int y=q.front().second;
            q.pop();

            for(int k=0;k<4;k++){
                int nx = x+dx[k];
                int ny = y+dy[k];
                if(nx>=1 && nx<=n && ny>=1 && ny<=n && visited[nx][ny]!=-1){
                    
                    if(visited[nx][ny]==1){
                        cout<<count-1<<endl;
                        return 0;
                    }
                    else{
                        visited[nx][ny]=-1;
                        q.push({nx,ny});
                    }
                }
            }
            
            
            
        }
        
    }

    
    
}