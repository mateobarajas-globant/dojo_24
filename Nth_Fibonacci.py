def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 3
print(fibonacci(n))

n = 6
print(fibonacci(n))