def diagDifference(m):
    n = len(m)
    first_sum = sum(m[i][i] for i in range(n))
    last_sum = sum(m[i][n - 1 - i] for i in range(n))
    
    return abs(first_sum - last_sum)

m = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

print(diagDifference(m))
                              