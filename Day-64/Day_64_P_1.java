/*


Mr Febin is working with numbers.
He wants to find all the AD Numbers,
An AD Number is defined as follows:
	- All the adjacent digits in the given number N 
	should have an absolute difference of 1 only. 

You will be given two integers, start and end,
Your task is to find all the AD Numbers in ascending order
in the range of [start, end], where both are inclusive.

Constarint:
----------
0 <= start < end <2*10^9.

Input Format:
-------------
Two space separated intergers,  start and end.

Output Format:
--------------
Print a list of integers.


Sample Input-1:
---------------
0 15

Sample Output-1:
----------------
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]


Sample Input-2:
---------------
25 65

Sample Output-2:
----------------
[32, 34, 43, 45, 54, 56, 65]




*/

//Solution:
import java.util.*;

class Day_64_P_1
{
	public static void Numbers(int n,int m,int AdjNum, ArrayList<Integer> answer)
	{
		if (AdjNum <= m && AdjNum >= n)
			answer.add(AdjNum);

		if (AdjNum == 0 || AdjNum > m)
			return ;

		int end = AdjNum % 10;

		int AdjNumA = AdjNum*10 + (end-1);
		int AdjNumB = AdjNum*10 + (end+1);

		if (end == 0)
			Numbers(n, m, AdjNumB, answer);

		else if(end == 9)
			Numbers(n, m, AdjNumA, answer);
		else
		{
			Numbers(n, m, AdjNumA, answer);
			Numbers(n, m, AdjNumB, answer);
		}
	}
	
	public static void main(String args[])
	{
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<Integer> answer = new ArrayList<Integer>();

		for (int i = 0 ; i <= 9 ; i++)
			Numbers(n, m, i, answer);
		
		Collections.sort(answer);
        for(int i=0; i<answer.size(); i++) {
            System.out.print(answer.get(i) + " ");
        }
	}
}

