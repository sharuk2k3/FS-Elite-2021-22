/*
Rahul works in a Water purifying plant.His job is to pack the water bottles of 
different sizes in a box.He packed the water bottles in different boxes.Each box
may have different number of bottles and the count is printed on the box.

Rahul asked Suresh to send these bottles in a grid(0-indexed) where one box can
be placed in one cell.
grid[i][j] represents the count printed on the box placed on cell (i,j)

Given a shift value 's' , Suresh has to shift the boxes 's' times in the grid.

In one shift , he can move:
   -grid[i][j] to grid[i][j+1]
   -grid[i][q-1] to grid[i+1][0]
   -grid[p-1][q-1] to grid[0][0].
Return the 2D-grid after shifting.

Input Format:
 -------------
 Line -1: 3 space seperated integers p , q and s represents number of rows ,number of columns and number of shifts..
 next p-Lines: q Space separated integers represents count printed on the box. 

Output Format:
 --------------
 Print a 2D array, 
  
Sample Input -1:
-------------
3 3 2
2 3 4
5 6 7
8 9 10
    
Sample Output -1:
--------------
9 10 2 
3 4 5 
6 7 8 
    
Explanation:
 -----------
As s=2, Every value is shifted forward 2 times.
grid[0][0]=2 is shifted to grid[0][2], grid[0][1]=3 is shifted to grid[1][0] and so on...

  
Sample Input-2:
-------------
4 5 3
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
5 4 2 3 1
    
Sample Output-2:
--------------
2 3 1 1 2 
3 4 5 6 7 
8 9 10 11 12 
13 14 15 5 4 
    

*/

#include<bits/stdc++.h>

using namespace std;

int main(){
    
    int p,q,s;
    cin>>p>>q>>s;
    vector<vector<int>> mat(p,vector<int>(q));
    for(int i=0;i<p;i++){
        for(int j=0;j<q;j++){
            cin>>mat[i][j];
        }
    }
    
    //vector<vector<int>> mat;
    vector<vector<int>> temp;
        temp = mat;
        int n = mat.size();
        int m = mat[0].size();
        while(s--){
            for(int i=0;i<n;++i){
                for(int j=1;j<m;++j){
                    temp[i][j]=mat[i][j-1];
                }
                    
            }
            for(int i=0;i<n-1;++i){
                temp[i+1][0]=mat[i][m-1];
            }
            temp[0][0]=mat[n-1][m-1]; 
            mat = temp;
        }
        
        for(int i=0;i<n;i++){
            cout<<"\n";
            for(int j=0;j<m;j++){
                cout<<temp[i][j]<<" ";
            }
        }
        
    }