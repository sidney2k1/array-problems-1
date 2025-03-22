def missingno(arr):
    n=len(arr)
    totalsum=(n+1)*(n+2)/2
    sumofarr=sum(arr)
    return totalsum-sumofarr
arr=[1,2,3]
print("Missing number:",missingno(arr))
