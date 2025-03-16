def leader(a,asize):
    currentmax=a[asize-1]
    print(currentmax)
    for i in range(asize-2,-1,-1):
        if currentmax<a[i]:
            print(a[i])
            currentmax=a[i]
a=[19,15,24,12,65,32,13,6]
leader(a,len(a))