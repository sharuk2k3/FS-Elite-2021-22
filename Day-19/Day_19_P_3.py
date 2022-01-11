'''

Gnanesh is working on Machine Learning domain. He wants train the machine 
in such a way that, if he provided an image printed with a string on it,
the machine has to extract the text as a string and verify that, 
after shuffling  the letters in the string, 'the shuffled string should be 
like no two adjacent letters should be same' 

You will be given extracted string, and
Can you help Gnanesh to train the machine with the given constraint 
The machine has to print "true", if the constarint is met, 
Otherwise, print "false".

Input Format:
-------------
A String S

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
aaabd

Sample Output-1:
----------------
true

Sample Input-2:
---------------
aaab

Sample Output-2:
----------------
false


'''


#SOLUTION

#USING HEAP

from collections import Counter
import heapq
def String(S):
    char_count = Counter(S)
    heap = [(-count, key) for key, count in char_count.items()]
    heapq.heapify(heap)
    ans = ""
        
    while heap:
        _, first_char = heapq.heappop(heap)
        second_char = ""
            
        if heap:
            _, second_char = heapq.heappop(heap)
                  
        if not ans:
            ans = first_char + second_char
        elif ans[-1] == first_char and (ans[-1] == second_char or second_char == ""):
            return False
        elif ans[-1] == first_char:
            ans += second_char + first_char
        else:
            ans += first_char + second_char
            
        char_count[first_char] -= 1
        if char_count[first_char] > 0:
            heapq.heappush(heap, (-char_count[first_char], first_char))
                
        char_count[second_char] -= 1
        if char_count[second_char] > 0:
            heapq.heappush(heap, (-char_count[second_char], second_char))
            
    return True
S=input()
print(String(S))


#NAVIE SOLUTION
'''
s=input()
cnt=0
for i in set(s):
    if s.count(i)>len(s)//2+len(s)%2:
        print("False")
        cnt=1
        break
if cnt==0:
    print("True")
'''