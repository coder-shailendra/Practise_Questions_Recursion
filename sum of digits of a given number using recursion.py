def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
num = 12345678
print(sum_digits(num))