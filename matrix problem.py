def row_sum(matrix):
    sums = []
   
    for row in matrix:
        total = 0
        for num in row:
            total += num
        sums.append(total)
        
    return sums
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(row_sum(matrix))
