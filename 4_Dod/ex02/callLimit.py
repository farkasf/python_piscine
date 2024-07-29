from typing import Any


def callLimit(limit: int):
    '''
    [CALLLIMIT] Returns a decorator that tracks
    the number of times a function is called and
    limits it to a specified value.
    '''
    count = 0

    def callLimiter(function):
        '''
        [CALLLIMITER] Limits the number of calls
        to the decorated function to the specified
        limit.
        '''

        def limit_function(*args: Any, **kwds: Any):
            '''
            [LIMIT_FUNCTION] Executes the decorated
            function if the call count is less or equal
            to the limit. Prints an error message if the
            limit is exceeded.
            '''
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return
        return limit_function

    return callLimiter
