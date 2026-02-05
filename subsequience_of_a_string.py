def return_subsequences(s1):
    if (s1 ==""):
        ans = [""]
        return ans
    smallans = return_subsequences(s1[1:])
    mychar = s1[0]
    ans = []
    ans.extend(smallans)
    for eachpermutation in smallans:
        ans.append(mychar + eachpermutation)
    return ans

s1 = "abc"
l1 = return_subsequences(s1)
print(l1)