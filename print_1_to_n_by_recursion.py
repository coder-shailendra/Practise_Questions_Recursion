def print1ToN(n):
    if n <= 0:
        return 0
    print1ToN(n-1)
    print(n)

print1ToN(20)