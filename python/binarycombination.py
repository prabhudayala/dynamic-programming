#all binary possibilities using backtracking a form of recurssion
A=[0]*3
def printBinary(n):
    if(n<1):
        print(A)
    else:
        A[n-1]=0
        printBinary(n-1)
        A[n-1]=1
        printBinary(n-1)
printBinary(3)
