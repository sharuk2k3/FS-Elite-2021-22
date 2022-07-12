'''

There are a series of bulbs numbered from 1 to n and initially all bulbs are 
turned off.

Now there are n istructions to be followed sequentially which are represented 
in an array a[],where a[i] is the value where you have to turn on a[i]-th bulb
in the series.

After every instructions you need to find a contiguous series of bulbs which 
are turned on such that it cannot be extended in either direction.

Given an integer k return the recent instruction at which there exists exactly 
'k'contiguous series of bulbs. If no such series exists, return -1.

Input Format:
-------------
Line-1: an integer n represents the number of instructions
Line-2: n space seperated integers represents instructions to be followed sequentially.
Line-3: An integer k.

Output Format:
--------------
return an integer represents recent instruction number.

Sample Input-1:
---------------
5
3 5 1 2 4
1

Sample Output-1:
----------------
4

Explanation:
------------
Step 1: "00100", sets: ["1"]
Step 2: "00101", sets: ["1", "1"]
Step 3: "10101", sets: ["1", "1", "1"]
Step 4: "11101", sets: ["111", "1"]
Step 5: "11111", sets: ["11111"]
The recent step at which there exists a group of size 1 is step 4.


Sample Input-2:
---------------
5
3 1 5 4 2
2

Sample Output-2:
----------------
-1

Explanation:
-------------
Step 1: "00100", sets: ["1"]
Step 2: "10100", sets: ["1", "1"]
Step 3: "10101", sets: ["1", "1", "1"]
Step 4: "10111", sets: ["1", "111"]
Step 5: "11111", sets: ["11111"]
No group of size 2 exists during any step.



'''

#Solution:



from collections import defaultdict

def findLatestStep(arr, m) :
        
    size = len(arr)
    if size == m:
        return size
    counter_of_len = defaultdict(lambda :0)
        
    len_of_cont_1s = [0] * ( size + 2 )    
        
    last_good_step = -1
    for step, cur_idx in enumerate(arr, 1):
            
        left_1s_length = len_of_cont_1s[cur_idx - 1]
        right_1s_length = len_of_cont_1s[cur_idx + 1]
            
        combined_1s_length = left_1s_length + 1 + right_1s_length
            
        len_of_cont_1s[cur_idx - left_1s_length] = combined_1s_length
        len_of_cont_1s[cur_idx + right_1s_length] = combined_1s_length
            
        counter_of_len[combined_1s_length] += 1
        counter_of_len[left_1s_length] -= 1
        counter_of_len[right_1s_length] -= 1
                
                
        if counter_of_len[m] > 0:
            last_good_step = step
        
        
    return last_good_step

if __name__ == "__main__" :
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    print(findLatestStep(arr, m))