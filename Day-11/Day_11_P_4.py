'''
JVS Infra Pvt Ltd purchased a flatland of size M*N, and it is divided into 1*1 cells.
They mave marked some cells with red colors indicated with 1.
and other cells with blue color indicated with 0.

They want build the walls in the form of rectangles by connecting four distinct 
red colored cells on the flatland that forms an axis-aligned rectangle.
And only the corners of the walls need to be red colored.

Your task is to help, JVS Infra to count the number of rectangular walls
can be built by connecting the red colored cells on the flatland.

Input Format:
-------------
Line-1: Two space separated integers, M and N
Next M lines: N space separated integers, either 0 or 1 only.

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
3 4
1 0 1 0
1 1 1 1
0 1 1 1

Sample Output-1:
----------------
4

Explanation:
-----------
Given flatland is:
1 0 1 0
1 1 1 1
0 1 1 1
Number of rectngular walls are: 4
rectangle-1: by connecting 1's at (0, 0), (1, 0), (0, 2), (1, 2)
rectangle-2: by connecting 1's at (1, 1), (1, 2), (2, 1), (2, 2)
rectangle-3: by connecting 1's at (1, 1), (1, 3), (2, 1), (2, 3)
rectangle-4: by connecting 1's at (1, 2), (2, 2), (1, 3), (2, 3)


Sample Input-2:
---------------
4 5
1 0 1 0 1
0 0 0 1 0
0 1 1 0 1
1 0 1 0 0

Sample Output-2:
----------------
2

'''

#SOLUTION

'''

#CPP SOL

#include<bits/stdc++.h> 

using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int grid[n][m];
    for(int i=0;i<n;i++)
        for(int j = 0;j<m;j++)
            cin>>grid[i][j];
    map<pair<int,int>,int> mp;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<m;j++){
            if(grid[i][j]==0) continue;
            for(int k=i+1;k<n;k++){
                if(grid[k][j]==1){
                    mp[{i,k}]++;
                }
            }
        }
    }
    int ans = 0;
    for(auto it: mp){
        ans += (it.second * (it.second - 1))/2;
    }
    cout<<ans<<endl;
    return 0;
}


'''

import collections

def countRectangles(grid):
    ends, res = collections.defaultdict(int), 0
    for row in grid:
        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                if row[i] and row[j]:
                    ends[(i, j)] = ends.get((i, j), 0) + 1
                    res += ends[(i, j)] - 1
    return res
n, m = map(int, input().split())
grid = []
for i in range(n):
    l = list(map(int, input().split()))
    grid.append(l)
if __name__=="__main__":
    print(countRectangles(grid))
