"""

Faulty Keyboard
Problem Description
Mr. Wick has a faulty keyboard. Some of the keys of the keyboard don't work. So, he has copied all those characters corresponding to the faulty keys on a clipboard from some existing document. Whenever those characters need to be typed, he pastes it from the clipboard. In typing whatever is required he needs to make use of paste, backspace and cursor traversal operations. Help him to minimize the number of operations he needs to do to complete his typing assignment. Each operation has one unit weightage.

Mr. Wick prefers verbal clarity over optimization of labour. That's why he prefers to fully process one word before processing the next word. This preference of his is very important to be honoured. Please see Example 1 in the examples section for better understanding.

Constraints
1 <= T <= 10^4

1 <= S <= 16

String T and S will only be comprised of letters a-z and digits 0-9

Input
First line contains text T to be typed

Second line contains string S of all the faulty keys pasted on clipboard

Output
Print the minimum number of operations required for typing the text T

Time Limit
1

Examples
Example 1

Input

experience was ultimate

ew

Output

14

Explanation

experience =(2+2+2+2) =[ {p+b} + {p+b} +{p+b} +{p+b} ]

was=(4)=[ p+m+b+m]

ultimate=(2)=[ p+b ]

where p=paste, b=backspace, m= move cursor

This is the right answer according to Mr. Wick's preference. However, this can also be done in another way. Since, this method does not honour Mr. Wick's preference this will be the wrong answer.

experiencew  =(2+2+2+1) =[ {p+b} + {p+b} +{p+b} +{p}]

as =(0) =[]

ultimate=(2)=[ p+b ]

By this method the number of operations is only 9. However, this violates the constraint of fully processing one word before processing the next word. Hence, this is the wrong answer.



Example 2

Input

supreme court is the highest judicial court

su

Output

17

Explanation

supreme =(1) =[ p]

court=(4)=[ p+m+b+m]

is=(2)=[ p+b ]

the=(0)

highest=(2)= [p+b]

judicial=(4)= [p+m+b+m]

court=(4)= [p+m+b+m]

"""

#SOLUTIONS
