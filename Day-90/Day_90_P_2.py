'''

There are N cities in a state.
The cities are connected with two types of roadways:
1) concrete roadway 2) asphalt roadway.
The roadways may be parallel.

You are given the lists of concrete roadways and asphalt roadways
between the cities. All roadways are unidirectional.
Concrete_Roadway[i,j] indiactes: a concrete road from city-i to city-j. Similarly,
Asphalt[i,j] indiactes: an asphalt road from city-i to city-j. Similarly,

Your task is to find and return the list of lengths of the shortest paths from 
city-0 to city-P, where P start from 0 to N-1. And the path should contains 
alternative roadways like as follows: concrete - asphalt - concrete -asphalt --etc
or vice versa. If there is no such shortest path exist print -1.

Input Format:
-------------
Line-1: 3 space separated integers N, C & A, Number of cities, routes between the cities.
		number of concrete roads and number of asphalt roads
Next C lines: Two space separated integers, concrete road between city-i to city-j.		
Next A lines: Two space separated integers, asphalt road between city-i to city-j.		

Output Format:
--------------
Print the list of lengths, the shortest paths.


Sample Input-1:
---------------
4 2 1
0 1
2 3
1 2

Sample Output-1:
----------------
0 1 2 3

Sample Input-2:
---------------
4 2 1
1 0
2 3
1 2

Sample Output-2:
----------------
0 -1 -1 -1


Sample Input-3:
---------------
4 3 2
1 0
1 2
2 3
0 1
1 2

Sample Output-3:
----------------
0 1 2 -1


'''

#Solution:

'''
#CPP Code:

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n,c,a;
    cin>>n>>c>>a;
    
    vector<vector<pair<int,int>>> temp(n+2);
    for(int i=0;i<c;i++){
        int u,v;
        cin>>u>>v;
        
        temp[u].push_back({v,0});
    }
    
    
    for(int i=0;i<a;i++){
        int u,v;
        cin>>u>>v;
        temp[u].push_back({v,1});
    }
    
    vector<vector<int>> visited(n+2,vector<int>(2,0));
    vector<vector<int>> distance(n+2,vector<int>(2,INT_MAX));
    queue<pair<int,int>> q;
    visited[0][0]=1;
    visited[0][1]=1;
    distance[0][0]=0;
    distance[0][1]=0;
    q.push({0,0});
    q.push({0,1});
    int count=0;
    while(!q.empty()){
        count++;
        int size = q.size();
        for(int i=0;i<size;i++){
            pair<int,int> p = q.front();
            q.pop();
            
            int src = p.first;
            int prev = p.second;
            for(auto& x: temp[src]){
                if(x.second!=prev && (visited[x.first][x.second]==0)){
                    
                    visited[x.first][x.second]=1;
                    distance[x.first][x.second]=count;
                    
                    q.push({x.first,x.second});
                }
            }
            
            
        }
        
        
        
    }
    for(int i=0;i<n;i++){
        int ans=INT_MAX;
    
        if(1){
            ans=min(ans,distance[i][0]);
        }
        if(1){
            ans=min(ans,distance[i][1]);
        }
        if(ans==INT_MAX){
            cout<<-1<<" ";
            continue;
        }
        cout<<min(distance[i][0],distance[i][1])<<" ";
    }
    cout<<endl;
    
    
    
}

'''