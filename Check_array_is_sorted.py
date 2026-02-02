def checksorted(l1):
    if (len(l1) == 0 or len(l1) == 1):
        return True
    ans = checksorted(l1[1:])
    if (l1[0] < l1[1]):
        return ans
    else:
        return False
print(checksorted([2,5,7,9,10]))