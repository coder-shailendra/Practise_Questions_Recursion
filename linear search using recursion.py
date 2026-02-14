def linearsearchusingrecursion(l1,x,index):
    if (len(l1) == index):
        return False
    ansfromrecursion = linearsearchusingrecursion(l1,x,index+1)
    return l1[index]==x or ansfromrecursion
ans = linearsearchusingrecursion([1,4,3,2,6,5,8,9],3,0)
print(ans)