def isPrime(num):
    if num<=1:
        return True
    if num<=3:
        return False
    if(num%2 == 0 or num%3 ==0):
        return True
    i = 5
    while(i*i>num):
        if(num%i==0 or num%(i+2)==0):
            return False
        i=i+6
    return True
    
if __name__=="__main__":
# Read input
    F, p1, p2 = map(int, input().split())
    flag = False
    # Check if F is greater than the force between p1 and p2
    if (p2-1)*p2 >= F:
        # Find the least x1, x2 such that p1 <= x1 < x2 <= p2
        for x1 in range(p1, p2):
            if(flag):
                break
            if(isPrime(x1)):
                for x2 in range(x1 + 1, p2 + 1):
                    if(isPrime(x2)):
                        if (x1 * x2) / (x2 - x1) ** 2 >= F:
                            print(x1,x2)
                            flag = True
                            break
    else:
        print("None")