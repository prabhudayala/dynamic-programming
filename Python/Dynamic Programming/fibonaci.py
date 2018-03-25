#recursive approach
def fibonaci(n):
    if n==0:return 1
    elif n==1:return 1;
    else: return fibonaci(n-1)+fibonaci(n-2)
print(fibonaci(7))


#bottom up approach
def fibonaci(n):
    fib_table=[0,1]
    for i in range(2,n+1):
        fib_table.append(fib_table[i-1]+fib_table[i-2])
        print(fib_table)
    return fib_table[n]
print(fibonaci(8))


#top down approach #1
def fibonaci(n):
    dictionary={1:1,2:1}
    if(n<=2):
        return 1
    if n in dictionary: 
        return dictionary[n]
    else: 
        dictionary[n]=fibonaci(n-1)+fibonaci(n-2)
        return dictionary[n]
print(fibonaci(8))

#top down approach #2
# storing only last 2 values to decrease space complexity
def fibonaci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
print(fibonaci(8))
