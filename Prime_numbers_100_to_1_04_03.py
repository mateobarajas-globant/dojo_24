def list_primes(start, end):
    if start < end: 
        return
    if start == end:
        if is_prime(start):
            print(start)
        return
    if is_prime(start): 
        print(start)
    list_primes(start - 1, end)

def is_prime(num, div=2):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % div == 0:
        return False
    if div * div > num:
        return True
    return is_prime(num, div + 1)

list_primes(100, 1)
