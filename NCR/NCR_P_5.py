'''
Program-7:
========
Given an array of scores of players  and a number K.
Give ranks to the scores.
same scores get same rank. Do not consider zero scores.
lower scores get rank based on their place.
find the count of players whose ranks<=k.
ex:
100 50 50 25  has ranks 1 2 2 4
for k=3 
ans:3
'''
def countElements(R, N, arr):
    arr.sort(reverse = True)
    rank = 1
    count = 0
    prevScore = arr[0]
    for score in arr:
        if score < prevScore:
            rank = count + 1
        if rank > R:
            break
        count += 1
        prevScore = score
    return count
 
arr=list(map(int,input().split()))
R=int(input())
N=len(arr)
print(countElements(R, N, arr))