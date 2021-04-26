# Write a function that will return the factorial of a given number

def factorial(a):
    result = 1
    for c in range(1, a + 1):
        result *= c

    return result


print(factorial(10))
