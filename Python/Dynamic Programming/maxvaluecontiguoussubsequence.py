#noraml approach
def maxvaluecontiguoussubsequence(a):
    length=len(a)
    msum=0
    for i in range(length):
        csum=0
        for j in range(i,length):
            csum+=a[j]
            if(csum>msum):
                msum=csum
    return msum
A=[-2,11,-4,13,-5,2]
B=[1,-3,4,-2,-1,6]
print(maxvaluecontiguoussubsequence(A))
print(maxvaluecontiguoussubsequence(B))



#Dp approach
def maxvaluecontiguoussubsequence(a):
    maxSum=0
    length=len(a)
    m=[0]*(length+1)
    if(a[0]>0):
        m[0]=a[0]
    else:
        m[0]=0
    for i in range (1,length):
        if m[i-1]+a[i]>0:
            m[i]=m[i-1]+a[i]
        else:
            m[i]=0
    for i in range(len(m)):
        if m[i]>maxSum:
            maxSum=m[i]
    return maxSum
A=[-2,11,-4,13,-5,2]
B=[1,-3,4,-2,-1,6]
print(maxvaluecontiguoussubsequence(A))
print(maxvaluecontiguoussubsequence(B))