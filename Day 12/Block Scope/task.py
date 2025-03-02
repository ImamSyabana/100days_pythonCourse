def is_prime(num):
    import math
    if num < 2:
        return False  # 0 and 1 are not prime numbers

    for factors in range(2, int(math.sqrt(num)) + 1):  # Only check up to sqrt(num)
        if num % factors == 0:
            return False  # Found a divisor, so it's not prime

    return True  # If no divisors found, it's prime
