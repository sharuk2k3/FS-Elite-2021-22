'''
Program-4:
========
There is an array of priorities that range from 1 to 99. The priorities should be 
reassigned such that the element which has the maximum priority should be minimized 
keeping the relative priorities with other elements the same

Sample Test Case 1
Input
1 4 8 4
Output
1 2 3 2

Sample Test Case 2
Input
1 3 7 3
Output
1 2 3 2
'''
import heapq
def getPriorities(p):
    n = len(p)
    heap = []

    for i in range(n):
        heapq.heappush(heap, (p[i], i))

    priority = 0
    prevNumber = 0

    while len(heap) > 0:
        popped = heapq.heappop(heap)
    
        if prevNumber != popped[0]:
            priority += 1
            prevNumber = popped[0]
    
        p[popped[1]] = priority

    return p
p=list(map(int,input().split()))
print(getPriorities(p))