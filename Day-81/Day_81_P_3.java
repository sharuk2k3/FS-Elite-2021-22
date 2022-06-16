/*

Mr Shravan is playing a Match-the-Pair Game.

Initially, He is given two teams team1 and team2.

Each team has some persons in it, each person is identified with an ID,

ID's are positive numbers, duplicates are allowed.



Your task is to match the persons from team1 to team2.

Team1 consist of M persons and Team2 consist of N persons.

And the rules for matching the persons are as follows:

	- You are allowed to match the persons from team1 with team2,

	only if the IDs are equal and you have to draw a line between the pair.

	- You are not allowed draw the line which is passing through another line.

	- If you are not allowed to draw the line, you cannot match the pair.

	- Each person must connected with atmost one person only.



Finally, count the maximum numbers of pairs can be formed between the teams.





Input Format:

-------------

Line-1: Two space separated integers, M and N.

Line-2: M space separated integers, team1[].

Line-3: N space separated integers, team2[]. 



Output Format:

--------------

Print an integer result.





Sample Input-1:

---------------

4 4

1 2 3 5

3 1 5 2



Sample Output-1:

----------------

2



Explanation: 

------------

You can Match the pair as follows: 

S1 - team1[0]-team2[1], team1[1]-team2[3]

S2 - team1[0]-team2[1], team1[3]-team2[2]

S3 - team1[2]-team2[0], team1[3]-team2[2]

In S1 you cannot match 3 with 3 or 5 with 5, because you are

not allowed to draw a line. same for S2 and S3.





Sample Input-2:

---------------

6 7

6 5 2 4 2 5

2 5 3 4 6 2 4



Sample Output-2:

----------------

3


*/


import java.util.*;

class Day_81_P_3{
    
    public static int rep(int i,int j,int n,int m,int[][] dp,int[] arr1,int[] arr2){
        
        if(i==n){
            return 0;
        }
        if(j==m){
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        
        int index=j;
        while(index<m && arr2[index]!=arr1[i]){
            index++;
        }
        
        if(index==m){
            return dp[i][j]=rep(i+1,j,n,m,dp,arr1,arr2);
        }
        else{
            return dp[i][j]=Math.max(1+rep(i+1,index+1,n,m,dp,arr1,arr2),rep(i+1,j,n,m,dp,arr1,arr2));
        }
        
        
        
    }
    
    public static void main(String[] args){
        
        int n,m;
        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt();
        m = sc.nextInt();
        
        int[] arr1 = new int[n];
        int[] arr2 = new int[m];
        for(int i=0;i<n;i++){
            arr1[i]=sc.nextInt();
        }
        
        for(int j=0;j<m;j++){
            arr2[j]=sc.nextInt();
        }
        
        int[][] dp = new int[n+2][m+2];
        for(int i=0;i<=n;i++){
            for(int j=0;j<=m;j++){
                dp[i][j]=-1;
            }
        }
        
        System.out.println(rep(0,0,n,m,dp,arr1,arr2));
        
        
    }
    
}