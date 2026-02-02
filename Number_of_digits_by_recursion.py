def number_of_digit(n):
    if (n >= 1 and n <= 9):
        return 1 
    elif n == 0:
        return 1
    smallnumber = int(n/10)
    smallanswer = number_of_digit(smallnumber)
    ans = 1 + smallanswer 
    return ans       

print(number_of_digit(12345))
print(number_of_digit(886891))