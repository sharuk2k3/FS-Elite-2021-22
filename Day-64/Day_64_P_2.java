import java.util.Scanner;

/*


Jadav Payeng, "The Forest Man of India", 
started planting the seeds in a M*N grid land.
Each cell in the grid land is planted with a seed.
After few days, some seeds grow into saplings indicates with '1',
and the rest are dead seeds indicates with '0'.

One or more saplings are connected either horizontally, vertically or diagonally 
with each other, form a sapling-group. 
There may be zero more sapling-groups in the grid land.

Jadav Payeng wants to know the biggest sapling-group in that grid land.

You are given the M * N grid, filled with 0's and 1's.
You are task is to help Jadav Payeng to find the number of saplings in 
the largest sapling-group.

Input Format:
-------------
Line-1: Two integers M and N, the number of rows and columns in the grid-land.
Next M lines: contains N space-separated integers .

Output Format:
--------------
Print an integer, the number of saplings in the 
largest sapling-group in the given grid-land.

Sample Input-1:
---------------
5 4
0 0 1 1
0 0 1 0
0 1 1 0
0 1 0 0
1 1 0 0

Sample Output-1:
----------------
8


Sample Input-2:
---------------
5 5
0 1 1 1 1
0 0 0 0 1
1 1 0 0 0
1 1 0 1 1
0 0 0 1 0

Sample Output-2:
----------------
5




*/
/*

import java.util.*;
public class Day_64_P_2
{
  public static void main (String[]args)
  {
    Scanner sc = new Scanner (System.in);
    int m, n, i, j;
      m = sc.nextInt ();
      n = sc.nextInt ();
    int mat[][] = new int[m][n];
    int mat2[][] = new int[m][n];
    for (i = 0; i < m; i++)
      for (j = 0; j < n; j++)
	    mat[i][j] = sc.nextInt ();
    
    
    for (i = 0; i < m; i++)
      {
    	for (j = 0; j < n; j++)
    	  {
    	    System.out.print (mat2[i][j] + " ");
    	  }
	System.out.println ();
      }

  }
}

*/
class Day_64_P_2 {
    public int numEnclaves(int[][] grid) {
      int count = 0;
   
      int r = grid.length;
      int c = grid[0].length;
      boolean[][] visited = new boolean[r][c];
      
      for(int i=0;i<c;i++){
            if(grid[0][i]==1 && visited[0][i]==false){
                dfs(grid,visited,0,i);
            }
        }
        for(int i=0;i<r;i++){
            if(grid[i][0]==1 &&  visited[i][0]==false ){
                dfs(grid,visited,i,0);
            }
        }
        for(int i=0;i<r;i++){
            if(grid[i][c-1]==1 &&  visited[i][c-1]==false){
                dfs(grid,visited,i,c-1);
            }
        }
        for(int i=0;i<c;i++){
            if(grid[r-1][i]==1 &&  visited[r-1][i]==false){
                dfs(grid,visited,r-1,i);
            }
        }
      
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(grid[i][j]==1 && visited[i][j]==false){
                    count++;
                }
            }
        }
        return count;
     
    }
  
   public void dfs(int[][] grid, boolean[][] visited, int r, int c){
 
       if(r>=grid.length||r<0|c>=grid[0].length||c<0)return;
       if(visited[r][c]==true || grid[r][c]==0)return;
       visited[r][c]=true;
       dfs(grid, visited, r-1, c);
       dfs(grid, visited, r+1, c);
       dfs(grid, visited, r, c-1);
       dfs(grid, visited, r, c+1);

  }
  public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int m, n, i, j;
        m = sc.nextInt ();
        n = sc.nextInt ();
        int grid[][] = new int[m][n];
        for (i = 0; i < m; i++)
            for (j = 0; j < n; j++)
                grid[i][j] = sc.nextInt ();
  }
}