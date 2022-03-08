'''

#CISCO EXAM OFF CAMPUS

2. Keypad Fun
We all know the old mobile keypad format,



It was fun to press the key no. 2, three times to get the character 'C', similarly press the key no. 4, two times to get the character 'H'.

We are in a situation, where we have the sequence of the key pressed and we need to find the actual string which got typed.

 

As a great programmer, can you solve it programmatically?

 

Instructions on Keypad format:

1 ---> , @  (characters will repeat)

2 ---> A B C a b c 2

3 ---> D E F d e f 3

4 ---> G H I g h i 4

5 ---> J K L j k l 5

6 ---> M N O m n o 6

7 ---> P Q R S p q r s 7

8 ---> T U V t u v 8

9 ---> W X Y Z w x y z 9

0 ---> [space] 0

 

'_' is used to represent when the same key is pressed back to back.

Example1: 22_222     represents the string "BC".

Example2:55555555 represents character 'J'.

 

 

Here,

To get the character '2',  you need to press the key no.2, Seven times.

To get the character 'm', you need to press the key no.6, Four times.

 

Constraints:

Length of each string <= 105

N <= 105

 

Input Format:

The first line contains the number of test cases N.

Each test case contains a string with characters 0 to 9.

 

Output Format:

For each test case print the string representing decode of the keypad press.

 

Example1:

input:

1

22244444477777777222222666666

 

output:

Cisco

 

Explanation:

The key no.2, pressed 3 times will give the character 'C'

The key no.4, pressed 6 times will give the character 'i'

The key no.7, pressed 8 times will give the character 's'

The key no.2, pressed 6 times will give the character 'c'

The key no.6, pressed 6 times will give the character 'o'

 

Example2:

input:

2

22_2222222222226666644442222555555666666777777733333

442222444444

 

output:

Bangalore

Hai

 

'''

def keypad(S):
    d = {'1':',','11':'@','2':'A','22':'B','222':'C','2222':'a','22222':'b','222222':'c','2222222':'2', '3':'D','33':'E','333':'F','3333':'d','33333':'e','333333':'f','3333333':'3', 
    '4':'G','44':'H','444':'I','4444':'g','44444':'h','444444':i,'4444444':'4',
     '5':'J','55':'K','555':'L','5555':'j','55555':'k','555555':'l','5555555':'5', 
     '6':'M','66':'N','666':'O','6666':'m','66666':'n','666666':'o','6666666':'6', 
     '7':'P','77':'Q','777':'R','7777':'p','77777':'q','777777':'r','7777777':'s','77777777':'7', 
     '8':'T','88':'U','888':'V','8888':'t','88888':'u','888888':'v','8888888':'8',
     '9':'W','99':'X','999':'Y','9999':'Z','99999':'w','999999':'x','9999999':'y','99999999':'z','999999999':'9',
     '0':' ', '00':'0','_':''}
    
    

for t in range(int(input())):
    S = input()
    print(keypad(S))
