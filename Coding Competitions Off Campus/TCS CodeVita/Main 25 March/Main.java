import java.util.*; 
class Main
{

	static int mod = 1000000007;
	static int[][] dp = new int[55][55];

	static int NoofWays(int face, int throwsVal, int sum)
	{
		if (sum == 0 && throwsVal == 0)
		{
			return 1;
		}

		if (sum < 0 || throwsVal == 0)
		{
			return 0;
		}

		if (dp[throwsVal][sum] != -1)
		{
			return dp[throwsVal][sum];
		}

		int ans = 0;
		for (int i = 1; i <= face; i++)
		{
			ans += NoofWays(face, throwsVal - 1, sum - i);
		}

		return dp[throwsVal][sum] = ans;
	}

	public static void main(String[] args)
	{
	    Scanner sc=new Scanner(System.in);
	    int T = sc.nextInt();
	    int[] result = new int[T];
	    sc.nextLine();
	    for(int test = 0; test < T; test++){
	        int total = 0;
	        String s = sc.nextLine();
	        String[] s1 = s.split(" ");
    		int sum = Integer.parseInt(s1[0]);
    		int faces = Integer.parseInt(s1[1]);
    		for (int i = 0; i < 55; i++)
    		{
    			for (int j = 0; j < 55; j++)
    			{
    				dp[i][j] = -1;
    			}
    		}
    		for(int throwsVal = 1; throwsVal < sum+1; throwsVal++){
    		    total+=NoofWays(faces, throwsVal, sum);
    		}
    		result[test] = total;
	    }
	    for(int value = 0; value < T; value++){
	        System.out.println(result[value]);
	    }
	}
}