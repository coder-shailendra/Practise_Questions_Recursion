def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

n = 264
print("Reversed number:", reverse_num(n))
