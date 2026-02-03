def removecharacter(s1,ch):
    if (len(s1)== 0 or s1 == " "):
        return s1
    smallanswer = removecharacter(s1[1:],ch)
    if (s1[0] == ch):
        return smallanswer
    else:
        return s1[0] + smallanswer
s1 = "good morningzzz"
ans = removecharacter(s1,"z")
print(ans)