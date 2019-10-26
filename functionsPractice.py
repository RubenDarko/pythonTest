def primeNumber(number):
    index = 2
    if number >= 2:
        while number % index != 0:
            index = index + 1
        if index == number:
            return True
        else:
            return False
    else:
        return False


for prime in range(100000):
    if primeNumber(prime):
        print(prime)
