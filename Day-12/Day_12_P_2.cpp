/*'''

Brahmi and his gang was chased by group of police officers, unfortunately 
they all got locked up in a building consist of M*N rooms in the form of 
a grid. All the rooms are connected with  the adjacent rooms both horizontally
and vertically. There are few rooms for them to escape called as safe zones. 

Now help Brahmi and his gang to reach the safe zones in the building.

In the Building we have the rooms filled with following values: [0,-1,-2] 
where, -1 -> Danger zone (they should not enter into it).
0 -> Safe Zone (room to escape)
-2 -> a thief

Now create a method to print the grid after performing following step: 
Fill each room with one of the member from The Brahmi and his gang with 
the distance to its nearest safe zone.
If it is impossible to reach a safezone, fill with '-2' only.

Input Format:
-------------
Line-1 -> two integers M and N, size of the grid of rooms.
Next M Lines -> N space separated integers, from this set [-2,-1,0] only.

Output Format:
--------------
Print an integer as result.


Sample Input-1:
---------------
4 4
-2 -1 0 -2
-2 -2 -2 -1
-2 -1 -2 -1
0 -1 -2 -2

Sample Output-1:
----------------
3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4



'''
*/
#include<bits/stdc++.h>
using namespace std;
int n,m;

void dfs(int i,int j,vector<vector<int>>& visited,vector<vector<int>>& temp,int d){
    
    if(i+1<n && (visited[i+1][j]==0 || d<visited[i+1][j]) && temp[i+1][j]==-2 ){
        visited[i+1][j]=d;
        dfs(i+1,j,visited,temp,d+1);
    }
    
    if(i-1>=0 && (visited[i-1][j]==0 || d<visited[i-1][j]) && temp[i-1][j]==-2){
        visited[i-1][j]=d;
        dfs(i-1,j,visited,temp,d+1);
    }
    
    if(j+1<m && (visited[i][j+1]==0 || d<visited[i][j+1]) && temp[i][j+1]==-2){
        visited[i][j+1]=d;
        dfs(i,j+1,visited,temp,d+1);
    }
    
    if(j-1>=0 && (visited[i][j-1]==0 || d<visited[i][j-1]) && temp[i][j-1]==-2){
        visited[i][j-1]=d;
        dfs(i,j-1,visited,temp,d+1);
    }

    
    
    
    
}

int main(){
    
    
    cin>>n>>m;
    
    vector<vector<int>> temp(n,vector<int>(m,0));
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>temp[i][j];
        }
    }
    
    vector<vector<int>> visited(n,vector<int>(m,0));
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!temp[i][j]){
                dfs(i,j,visited,temp,1);
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!visited[i][j]){
                visited[i][j]=temp[i][j];
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<visited[i][j]<<" ";
        }
        cout<<endl;
    }
    
    
    
}