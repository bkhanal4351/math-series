"""
The function has one parameter n. The function returns the nth value in the fibonacci series.
"""
def fibonacci(n):
    if n in {0, 1}:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


"""
This function returns the nth value in the lucas numbers
"""


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


"""
This function has one required parameter and two optional parameter.
Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
Other values for the optional parameters will produce other series.
"""


def sum_series(n, first_num=0, second_num=1):
    if n == 0:
        return first_num
    elif n == 1:
        return second_num
    return sum_series(n-1, first_num, second_num) + sum_series(n-2, first_num, second_num)


