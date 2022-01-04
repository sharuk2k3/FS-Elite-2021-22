''''

M.P.Ahammed the founder of Malbar Gold and Diamonds merchant, announced an offer
that they will charge the minimum amount to make all the gold-biscuits into one.

Mr. Praveen, a gold supplier has different weighed gold-biscuits with him.
He wants to utilize the offer.

The processing charge to make two biscuits into one is calculated as follows:
	- To make two biscuits of weights A and B into one biscuit, 
	you have to pay the amount 'A + B'. 

Your task is to help M.P.Ahammed to keep his promise and 
to charge the minimum amount to make Mr. Praveen's gold-biscuits 
into one gold-biscuit.

Input Format:
-------------
Single line of space separated integers, number on the boxes.

Output Format:
--------------
Print an integer, minimum amount to be paid by Mr Shravan.


Sample Input-1:
---------------
4 3 6

4+3=7
7+6=13


Sample Output-1:
----------------
20


Sample Input-2:
---------------
5 2 4 3 6
5+2=7
7+4=11
11+3=14
14+6=20
7+11+14+20=

Sample Output-2:
----------------
45



'''

#SOLUTION


def func(lst):
    ans=[]
    while(len(lst)>1):
        lst.sort()
        ans.append(lst[0]+lst[1])
        lst[1]=lst[0]+lst[1]
        lst=lst[1:]
    return sum(ans)
lst=list(map(int,input().split()))
print(func(lst))