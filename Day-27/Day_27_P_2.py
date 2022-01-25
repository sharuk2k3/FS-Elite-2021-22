'''

EA Sports, developed a video game. They designed a game in such a way that, 
there are L number of levels from 1 to L. There are D number of dependencies
where each dependency[m] = [ Xm, Ym ], represents a prerequisite relationship,
that is, in order to play level-Ym, you must have completed the level-Xm.

In one day you can complete any number of levels as long as you 
have completed all the prerequisites levels in the game. 

You cannont play a level-Ym which has some prerequisite level-Xm on same day.

Write a method to return the minimum number of days to complete all the levels
in the game. If there is no way to complete all the levels, return -1.


Input Format:
-------------
Line-1: An integer L, number of levels.
Line-2: An integer D, number of dependencies.
Next D lines: Two space separated integers, Xm and Ym.

Output Format:
--------------
An integer, the minimum number of days to complete all the levels in the game.


Sample Input-1:
---------------
3
2
1 3
2 3

Sample Output-1:
----------------
2

Explanation-1:
--------------
On the first day, levels 1 and 2 are completed. 
On the second day, level-3 is completed.


Sample Input-2:
---------------
3
3
1 2
2 3
3 1

Sample Output-2:
----------------
-1

Explanation-2:
-------------
No level can be completed because they depend on each other.



'''

#CPP-Solution


'''
#include<bits/stdc++.h>

using namespace std;

 bool checkCycle(vector<vector<int>> &graph, int curr, vector<int> &visited){
        if(visited[curr] == 2){
            return true;
        }
        
        visited[curr] = 2;
        
        for(int i: graph[curr]){
            if(visited[i] != 1){
                bool ans;
                ans = checkCycle(graph, i, visited);
                if(ans == true){
                    return true;
                }
            }
        }
        
        visited[curr] = 1;
        return false;
    }


int get_ans(vector<vector<int>>& v,int n,vector<int>& indeg){
    
    vector<int> vis(n,0);
    int count = 0;
    queue<int> q;
    for(int i=0;i<n;i++){
        if(indeg[i]==0){
            q.push(i);
        }
    }
    for(int i=0;i<n;i++){
        if(checkCycle(v,i,vis)){
        return -1;
    }
    }
    while(!q.empty()){
        int s = q.size();
        for(int i=0;i<s;i++){
            int p = q.front();
            q.pop();
            for(auto ele:v[p]){
                    q.push(ele);
            }
        }
        count++;
    }
        return count;
    
}

int main(){
    
    int l;
    cin>>l;
    int d;
    cin>>d;
    vector<vector<int>> v(l,vector<int>());
    vector<int> indg(l,0);
    for(int i=0;i<d;i++){
        int x,y;
        cin>>x>>y;
        v[x-1].push_back(y-1);
        indg[y-1]++;
    }
    cout<<get_ans(v,l,indg);
    
    
}
'''