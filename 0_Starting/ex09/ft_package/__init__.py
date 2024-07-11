from .ft_filter import ft_filter


def count_in_list(iterable: list, to_find: str) -> int:
    '''
    [COUNT_IN_LIST] Counts occurrences of a string (to_find)
    in a list (iterable) using a filtering mechanism.
    '''
    filtered = ft_filter(lambda x: x == to_find, iterable)
    count = sum(1 for item in filtered)
    return count
