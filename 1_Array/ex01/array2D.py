import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    [SLICE_ME] verifies the correctness of the given input
    values, displays the shape of the 'family' array, slices
    it from the start to end indices and returns the sliced
    portion as a list
    '''
    try:
        if len(family) == 0:
            raise ValueError("'family' must not be empty")
        if type(family) is not list:
            raise TypeError("'family' must be a list")
        if not all(type(row) is list for row in family):
            raise TypeError("'family' must be a list of lists")
        if type(start) is not int or type(end) is not int:
            raise TypeError("'start' and 'end' must be integers")

        for member in family:
            if len(member) != len(family[0]):
                raise ValueError("lists members are not of the same size")

    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

    family_array = np.array(family)
    print(f"My shape is : {family_array.shape}")
    sliced = family_array[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()
