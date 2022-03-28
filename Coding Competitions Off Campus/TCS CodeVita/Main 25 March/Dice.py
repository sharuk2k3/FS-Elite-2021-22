import numpy as np

mod = 1000000007;

dp = np.zeros((55,55));

def NoofWays(face, throws, sum) :
	if (sum == 0 and throws == 0) :
		return 1;

	if (sum < 0 or throws == 0) :
		return 0;
	if (dp[throws][sum] != -1) :
		return dp[throws][sum];

	ans = 0;
	for i in range(1, face + 1) :
		ans += NoofWays(face, throws - 1, sum - i);
	dp[throws][sum] = ans;
	
	return int(ans);


if __name__ == "__main__" :
    t = int(input())
    result = []
    for t1 in range(t):
        sum,faces=map(int, input().split())
        total = 0
        for i in range(55) :
            for j in range(55) :
                dp[i][j] = -1
        for throws in range(1,sum+1):
            total += NoofWays(faces, throws, sum)
        result.append(total);
    print(*result,sep= '\n')
