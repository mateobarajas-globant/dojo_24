def print_primes(start, end):
    if start < end: 
        return
    if start == end:
        if is_prime(start):
            print(start)
        return
    if is_prime(start): 
        print(start)
    print_primes(start - 1, end)

def is_prime(num, divisor=2):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % divisor == 0:
        return False
    if divisor * divisor > num:
        return True
    return is_prime(num, divisor + 1)

print_primes(100, 1)
