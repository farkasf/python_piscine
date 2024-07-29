def square(x: int | float) -> int | float:
    '''
    [SQUARE] Returns the square of the given number.
    '''
    return x * x


def pow(x: int | float) -> int | float:
    '''
    [POW] Returns the result of raising the number to
    the power of itself.
    '''
    return x ** x


def outer(x: int | float, function) -> object:
    '''
    [OUTER] Returns a function that repeatedly applies
    the square/pow function to a value of x, which is
    updated with each call.
    '''
    count = 0

    def inner() -> float:
        '''
        [INNER] Calculates and returns the result of
        applying the square/pow function to the current
        value. Uses count to store and update the result
        of each operation.
        '''
        nonlocal count
        if count == 0:
            result = function(x)
        else:
            result = function(count)
        count = result
        return result

    return inner
