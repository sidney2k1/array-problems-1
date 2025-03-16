def rotations(a,n,asize):
    for i in range(n):
        rotate(a,asize)
def rotate(a,asize):
    temp=a[0]
    for i in range(asize-1):
        a[i]=a[i+1]
    a[asize-1]=temp
def printarray(a,asize):
    for i in range(asize):
        print("%d"%a[i],end=" ")
    print("\n")
a=[1,2,3,4,5,6,7,8,9]
printarray(a,len(a))
rotations(a,2,len(a))
printarray(a,len(a))