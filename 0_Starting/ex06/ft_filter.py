def ft_filter(function, iterable):
    '''
    [FT_FILTER] filters the given sequence with the help of a function
    that tests each element in the sequence to be true or not. If None
    is provided, it just returns the sequence.
    '''
    if function:
        return (x for x in iterable if function(x))
    else:
        return (x for x in iterable if x)
