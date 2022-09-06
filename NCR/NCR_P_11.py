'''
Program-1: Analogous array

There is a secret array.An array is said to be analogous array if
a) it has the same length as the secret array and
b) its elements lie between a given lowerbound and upperbound(both inclusive) and
c) the difference between consecutive elements in the given array is the same as the difference between 
the consecutive elements of the secret array.
i.e if secret_array[i-1]-secret_array[i]=analogous_array[i-1]-analogous_array[i]
Given lower bound,upper bound,size of the array and the list of consecutive elements' differences of 
the secret array,find the no.of analogous arrays possible.

Ex: lowerbound=2 upperbound=8
      size=4
      differences list=[-1 -3 2]
      Sol: If we consider 3 as the first element, the analogous array that can be constructed by making use of 
      the differences list is 
    3 , 3-(-1)=4 , 4-(-3)=7 , 7-2=5  ->Array formed : 3 4 7 5(all elements are in between given lowerbound and upperbound)
    similarly, by considering 2 as the first element,analogous array that can be formed is 2 , 2-(-1)=3 , 3-(-3)=6 , 6-2=4 ->
    Array formed: 2 3 6 4(lower,upperbound range satisfied)
    similarly, by considering 4 as the first element, the analogous array that can be formed is 4 , 4-(-1)=5 , 5-(-3)=8 , 8-2=6->
    Array formed: 4 5 8 6(lower,upper bound conditions also satisfied)
therefore 3 analogous arrays could be formed, hence return 3.
'''
def count_secret_pairs(ub,lb,cd) :
    hs = ls = sum = 0
    for value in cd:
        sum += value
        hs = max(sum, hs)
        ls = min(sum, ls)
    result = (ub - lb + (ls - hs + 1))
    if result < 0:
        return 0
    else:
        return result
cd=list(map(int,input().split()))
lb=int(input())
ub=int(input())
print(count_secret_pairs(ub,lb,cd))
