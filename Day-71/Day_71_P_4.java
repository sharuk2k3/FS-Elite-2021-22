/*

Keerthilal wants to try his luck in Diamonds business. 
He decides to buy and sell diamonds. 

He is given the prices of one diamond for N days by his friend.
Initially, it is assumed that he has no diamonds.

You need to help Keerthilal in making the maximum profit that is possible. 
He can sell a diamond only after he buys a diamond. 

Note: 
    - He is allowed to do any number of transactions
      but, he can buy and sell only one diamond per transaction.
    
    - He must complete one transaction before the next transaction.
    
    - After each transaction completed, there is a break day.
    i.e After he sells his diamond, he cannot buy diamond on next day.

		
Input Format:
-------------
Space separated integers, price of the diamond for N days.

Output Format:
--------------
Print an integer, maximum profit.


Sample Input-1:
---------------
7 1 5 3 6 4

Sample Output-1:
----------------
5

Explanation: 
------------
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


Sample Input-2:
---------------
1 2 3 1 3

Sample Output-2:
----------------
3

Explanation: 
------------
Buy on day 1 (price = 1) and sell on day 2 (price = 2), profit = 2-1 = 1.
Buy on day 4 (price = 1) and sell on day 5 (price = 3), profit = 3-1 = 2.
Total Maximum Profit = 1+2 = 3



*/

import java.util.*;

public class Day_71_P_4 {

    public static int getResult(int[] arr){
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;
        for(int i=0;i<arr.length;i++){
            if(arr[i]<minPrice){
                minPrice = arr[i];
            }
            if(arr[i]-minPrice>maxProfit){
                maxProfit = arr[i]-minPrice;
            }
        }
        return maxProfit;
    }
    public static void main(String... args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(getResult(arr));
    }
    
}
