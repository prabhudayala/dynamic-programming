#Tower of hanoi
#from to using auxilary == a to b using c
def tower(n,a,b,c):
    #if only one disk move it and stop
    if n==1:
        print("move disk 1 from %s to %s"%(a,b))
        return
    #move top n-1 disks from source to aux
    tower(n-1,a,c,b)
    print("move disk %d from peg %s to peg %s "%(n,a,b))
    #move n-1 disks from b to c using a as auxilary
    tower(n-1,c,b,a)
tower(4,"T1","T3","T2")

