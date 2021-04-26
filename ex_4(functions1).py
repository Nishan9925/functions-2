# Write a function that will return true if the number is bouquet and false if not. The result of function
# should be used in another one which will power up the number by 3


def is_even(number):
    result = False
    if number % 2 == 0:
        result = True

    return result


def pow_3(number):
    if is_even(number) == True:
        return number ** 3
    else:
        return "Number " + str(number) + " is not even"


print(pow_3(36))
