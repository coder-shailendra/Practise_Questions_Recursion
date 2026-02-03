def sumarray(l1):
    if (len(l1)==0):
        return 0
    sumofleftoverarray = sumarray(l1[1:])
    ans = sumofleftoverarray + l1[0]
    return ans

print(sumarray([1,2,3,4,5]))
