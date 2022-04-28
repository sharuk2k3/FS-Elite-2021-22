/*
'''

Arjun wants to build a swimming pool, in the backyard of his farm-house.
The backyard has an empty land of size m*n. 
Some part of the backyard is used to build the swimming pool
You will be given the m*n grid values (0's and 1's). 
where 1 indicates swimming pool, and 0 indiactes empty land.

Your task to find the perimeter of the swimming pool.

Note: There is only one swimming pool.

Input Format:
-------------
Line-1: Two integers M and N, size of the backyard.
Next M lines: N space separated integers, either 0 or 1
0- represents empty land and 1- represents the swimming pool 

Output Format:
--------------
Print an integer, the perimeter of the swimming pool


Sample Input-1:
---------------	
4 4
0 1 0 0
1 1 1 0
0 1 0 0
1 1 0 0
 
Sample Output-1:
----------------
16


Sample Input-2:
---------------
1 2
1 0
 
Sample Output-2:
----------------
4

For explanation of sample test cases given refer Hint-1.


'''

*/

#include<bits/stdc++.h>

using namespace std;

int dr[]={1,0,-1,0};
int dc[]={0,1,0,-1};


int main(){
	
	int n,m;
	cin>>n>>m;
	
	int a[n][m];
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>a[i][j];
		}
	}
	
	int ans=0;
	for(int i=0;i<n;i++){
		
		for(int j=0;j<m;j++){
			int cur=0;
			if (a[i][j]==1){
				cur+=4;
				for(int k=0;k<4;k++){
					int r = i+dr[k],c=j+dc[k];
					if (r<0 || c<0 || r>=n || c>=m) continue;
					if (a[r][c]==1) cur--;
				}
			}
			ans+=cur;
		}
	}
	
	cout<<ans<<endl;
	
	return 0;
}