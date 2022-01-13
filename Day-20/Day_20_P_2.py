'''

Somasekharam is given a 2D grid of size M*N, 
the grid is filled with integers in the range of 1 to 10000:
He need to findout the sum of the elements of the sub-grid inside
the given 2D grid defined by its upper left corner (r1,c1) and
lower right corner (r2, c2).
 
Create and Implement the NumGrid class as follows:
	- NumGrid(int[][] grid) 
		- initializes the object with the integer grid.
	- int sumOfSubGrid(int r1, int c1, int r2, int c2)
		- returns the sum of the elements of sub-grid inside 
		the sub-grid defined by its upper left corner (r1, c1) 
		and lower right corner (r2, c2) .

Somasekharam is given a 2d grid of size M*N and Q queries of sumOfSubGrid.
Your task is to help Somasekharam to create and implement the NumGrid class.

Constraints:
------------
1 <= M, N, Q <= 100
0 <= r1,r2 < M
0 <= c1,c2 < N
r1<=r2
c1<=c2
 
Input Format:
-------------
Line-1: Three space separated integers M,N and Q.
Next M lines: N space separated integers, values of arr[][].
Next Q lines: four space separated integers, r1, c1, r2, c2

Output Format:
--------------
Print Q lines of integers, the sum of the elements of sub-grid.


Sample Input-1:
---------------
6 5 4
12 7 20 17 13	// 2D Grid
16 15 9 7 15
1 18 14 12 10
17 7 12 14 4
2 18 3 16 17
7 6 7 13 8
1 3 5 4		// Queries
2 2 3 3
1 2 4 3
0 4 4 4

Sample Output-1:
----------------
116
52
87
59


'''

#CPP-SOLUTION

'''
#include<bits/stdc++.h>
using namespace std;

int n,m;

void update(int row,int col,int val,vector<vector<int>>& bit){
    int i=row;
    int j=col;
    while(i<=n){
        while(j<=m){
            bit[i][j]+=val;
            j=j+(j&(-j));
        }
        i=i+(i&(-i));
        j=col;
    }
    
    
}

int query(int i,int j,vector<vector<int>>& bit){
    
    int ans=0;
    while(i){
        int j1=j;
        while(j1){
            ans+=bit[i][j1];
            j1=j1-(j1&(-j1));
        }
        i=i-(i&(-i));
    }
    return ans;
    
}

int sum(int x1,int y1,int x2,int y2,vector<vector<int>>& bit){
    
    int fans = query(x2,y2,bit)-query(x2,y1-1,bit);
    fans-=query(x1-1,y2,bit);
    fans+=query(x1-1,y1-1,bit);
    
    return fans;
}


int main(){
    int q;
    cin>>n>>m>>q;
    
    vector<vector<int>> temp(n+1,vector<int>(m+1,0));
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            cin>>temp[i][j];
        }
        
    }
    
    vector<vector<int>> bit(n+1,vector<int>(m+1,0));
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            update(i,j,temp[i][j],bit);
        }
        
    }
    
    

    for(int i=0;i<q;i++){
        int x1,y1,x2,y2;
        cin>>x1>>y1>>x2>>y2;
        x1++;
        y1++;
        x2++;
        y2++;
        
        cout<<sum(x1,y1,x2,y2,bit)<<endl;
        
        
    }
    
    
}
'''