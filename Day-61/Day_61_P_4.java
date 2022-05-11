/*

You are given a bunch of sticks with diffrent lengths.
All the even length sticks should be arranged to appear first in the bunch and 
all the odd length sticks should be arranged to appear first in the bunch.

Print the length of the sticks, after arranging them according to above conditions. 

NOTE: The arrangement of sticks should be in order.

Input Format:
-------------
Line-1: An integer N, number of sticks in the bunch
Line-2: N comma separated integers, lengths of the sticks.

Output Format:
--------------
Print the list of length of the sticks after arrangements accordingly.


Sample Input:
-------------
4
1,4,3,2

Sample Output:
--------------
[4,2,1,3]


Sample Input-2:
---------------
10
4,8,5,4,9,8,9,9,1,8

Sample Output-2:
----------------
[4,8,4,8,8,5,9,9,9,1]



*/


import java.util.*;
import java.util.stream.Stream;
import java.util.function.Function;
import java.util.stream.Collectors;
public class Day_61_P_4{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        String inp[]=sc.next().split(",");
        for(int i=0;i<n;i++){
            arr[i]=Integer.parseInt(inp[i]);
        }
        List<Integer>ans=Arrays.stream(arr)
            .boxed()
            .filter(x->x%2==0)
            .collect(Collectors.toList());
        System.out.println(Arrays.stream(arr).boxed().filter(x->x%2==1).collect(Collectors.toCollection(()->ans)));
    }
}
