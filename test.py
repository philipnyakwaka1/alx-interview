#!/usr/bin/env python3
def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

number = 12
print("Prime factors of", number, "are:", prime_factors(number))
print(3//3)

