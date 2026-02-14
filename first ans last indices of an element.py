def firstindicesofanelement(l1,x):
    if (len(l1) == 0):
        return -1
    if (l1[0]==x):
        return 0 
    ansfromrecursion = firstindicesofanelement(l1[1:],x)
    if (ansfromrecursion==-1):
        return ansfromrecursion
    else:
        return ansfromrecursion + 1
    
print(firstindicesofanelement([3,2,5,2,8,2,1],2))
print(firstindicesofanelement([3,2,5,2,8,2,1],11))
print(firstindicesofanelement([3,2,5,2,8,2,1],3))
print(firstindicesofanelement([3,2,5,2,8,2,1],5))
print(firstindicesofanelement([3,2,5,2,8,2,1],1))