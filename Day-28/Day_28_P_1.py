'''

AMB mall to attract kids and to increase their economy they came to have 
a separate Fun Zone. They opened a stall by name Soda Bears. We have an 
LED display panel with different colours of Soda bears.

You will be given a 2D integer panel representing the grid of a 
Soda bears, we have different color-codes as positive integer in 
panel [p][q] of each coloured soda bears. If a cell in 
panel[p][q]=0 representing at position (p,q) is empty. 

The given panel represents the state of game according to participants move. 
Now it’s your aim to make panel to a stable state by merging Soda Bears 
with certain conditions:

1. If three or more soda bears of the same colour are adjacent 
vertically or horizontally,"merge" them all at the same time - 
these locations become empty.

2. After merging all Soda Bears simultaneously, if an empty space on
the panel has soda bears on top of itself, then these bears will drop
until they hit another bear or bottom at the same time. 
(No new soda bear will drop outside the top boundary.)

3. After the above steps, there may exist more bears that can be merged. 
If so, you need to repeat the above steps.

4. If there does not exist more bears for merge (ie. the panel is stable), 
then return the current panel.

Repeat the procedure for stable panel, then return the current panel state.

Input Format:
-------------
Line-1: Two space separated integers, M and N size of panel
Next M lines: N space separated integers, color codes of soda bears.

Output Format:
--------------
Print the stable format of panel.


Sample Input:
--------------
8 4
11 5 13 5
12 13 5 13
1 2 3 4
11 2 3 4
2 2 2 5
13 13 3 4
14 13 13 14
12 12 11 13

Sample Output:
----------------
0 0 0 5
11 0 0 13
12 0 0 4
1 0 0 4
11 0 13 5
13 0 5 4
14 5 13 14
12 12 11 13



'''

#SOLUTION

def ABM_Mall(soda):
    
    bear=False
    
    for i in range(m):
        for j in range(n-2):
            if abs(soda[i][j]) == abs (soda [ i][j+1]) == abs(soda[i][j+2]) !=0:
                (soda[i][j]) =(soda[i][j +1])= (soda[i][j+2])=-abs(soda[i][j])
                
                bear=True
            
    for i in range(m-2):
        for j in range(n) :
            if abs(soda[i][j]) == abs(soda[i+1][j]) == abs(soda[ i+2][j]) != 0:
                (soda[i][j])= (soda[i+1][j])= (soda[i+2][j])=- abs (soda [i][j])
                
                bear=True
            
    for j in range(n):
        panel=m-1
        
        for i in range(m-1,-1,-1):
            if soda[ i][j]>0:
                soda[panel][j]=soda[i][j]
                panel-=1
                
        for i in range (panel+1) :
            soda[i][j]=0
            
    return ABM_Mall(soda) if bear else soda
    
if __name__=="__main__":
    m,n=map(int,input().split())
    soda=[]
    for i in range(m):
        row=list(map(int,input().split()))
        soda.append(row)
    print(ABM_Mall(soda))