def fibonicci(n):
    if n == 0 or n == 1:
        return 1
    last = fibonicci(n - 1)
    second_last = fibonicci(n - 2)
    ans = last + second_last
    return ans
print(fibonicci(6))