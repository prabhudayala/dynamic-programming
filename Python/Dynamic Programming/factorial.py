#recursive approach 
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
	
	
#dp approach
dictionary={}
def factorial(n):
    try:
        return dictionary[n]
    except KeyError:
        if n==0:
            dictionary[0]=1
            return 1
        else:
            dictionary[n]=n*factorial(n-1)
            return dictionary[n]
print(factorial(5))

