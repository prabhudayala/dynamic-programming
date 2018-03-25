def myFunction(n):
    sum=0
    if n==0 or n==1: 
        return 2;
    for i in range(1,n):
        sum+=2*myFunction(i)*myFunction(i-1)
    return sum;
print(myFunction(5))


def myFunction(n):
    t=[0]*(n+1)
    t[0]=2
    t[1]=2
    #t[2]=2*t[1]*t[0]
    if n==0 or n==1: 
        return t[n];
    for i in range(2,n+1):
        for j in range (1,i):
            t[i]+=2*t[j]*t[j-1]
    return t[n];
print(myFunction(5))