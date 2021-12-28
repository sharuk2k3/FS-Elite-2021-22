'''

Bindu is passionated about clocks.
She found a digital clock, which has 2 rows of led lights,
Top row has 4-leds OOOO indicates hours (0-11).
Bottom row has 6-leds OOOOOO indicates minutes(0-59).
Where O -> led is OFF and * -> led is ON.

For Example: 
If the clock showing the led lights are as follows:
	OO*O indiactes a binary number, 0010 -> 2 hrs
	OO*O** indiactes a binary number, 001011 -> 11 minutes.
So, Time is 2:11

Now, you are given an integer N, number of led lights that are ON.
Your task is to find, all the  possible times in ascending order.

Format of time should be as follows:
	- Hours should not have leading 0's.
	- Minutes should be represented with 2 digits.

Suppose Current time is 1 hous 1 minute
	- Valid time is 1:01
	- Invalid time is as follows:- 01:1, 01:01, 1:1

Input Format:
-------------
An integer N, number of led lights ON.

Output Format:
--------------
Print the list of times in ascending order.


Sample Input:
---------------
1

Sample Output:
----------------
[0:01, 0:02, 0:04, 0:08, 0:16, 0:32, 1:00, 2:00, 4:00, 8:00]



'''


def Watch(turnedOn):
    res = []
    led = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
    def dfs(h, m, idx, n):
        if h > 11 or m > 59:
            return
        if n == 0:
            res.append("{:d}:{:02d}".format(h, m))
            return
        for i in range(idx, len(led)):
            if i <= 3:
                dfs(h + led[i], m, i + 1, n - 1)
            elif i < len(led):
                dfs(h, m + led[i], i + 1, n - 1)
    dfs(0, 0, 0, turnedOn)
    return sorted(res)
turnedOn=int(input())
if __name__=="__main__":
    print(Watch(turnedOn))
