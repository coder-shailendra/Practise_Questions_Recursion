def permutation(s):
    if len(s) == 0:
        return [""]
    small_ans = permutation(s[1:])
    ans = []

    for word in small_ans:
        for i in range(len(word) + 1):
            new_word = word[:i] + s[0] + word[i:]
            ans.append(new_word)

    return ans

s = "abc"
result = permutation(s)

for p in result:
    print(p)

