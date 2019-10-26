def primeNumber(number):
    index = 2
    if number >= 2:
        while number % index != 0:
            index = index + 1
        if index == number:
            return True
        return False
    return False


for prime in range(1000, 10000):
    if primeNumber(prime):
        print(prime)
