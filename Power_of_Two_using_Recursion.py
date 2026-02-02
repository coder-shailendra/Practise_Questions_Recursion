def power2(n):
    if (n == 1):
        return 2
    smallAnswer = power2(n-1)
    answer = 2 * smallAnswer
    return answer

print(power2(8))