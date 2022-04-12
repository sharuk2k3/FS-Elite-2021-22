'''

There is a switch-board made by an electrician,
If you turn on any two adjacent switches, it will cause short-circuit
and damage the switch-board.

You are given N integers(only 0's and 1's), Indiactes current status of the 
switch board with N switches, where 1 indiactes switch is ON and 0 indiactes 
switch is OFF. And an integer K, more number of switches to be turned ON.

Return true if and only if you can turn ON all the K switches, without causing 
any damage to switch-board. Otherwise return fasle.

Input Format:
-------------
Line-1: Two integers N and K, number of switches, and more K switches to be ON
Line-2: N space separated integers, only 0's and 1's.

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
5 1
1 0 0 0 1

Sample Output-1:
----------------
true

Sample Input-2:
---------------
5 2	
1 0 0 0 1

Sample Output-2:
----------------
flase


'''

#Solution:

def switchBoard(n, k, arr):
    i,j = 0,1
    while j != n:
        if arr[i] == 0 and arr[j] == 0:
            if arr[i-1] == 1 and i >= 0:
                i += 1
                j += 1
                continue
            arr[i] = 1
            k -= 1
        i += 1
        j += 1
    if k <= 0:
        return True
    else:
        return False

n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(switchBoard(n,k,arr))


