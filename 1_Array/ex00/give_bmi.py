import numpy as np


def check_array_type(array: np.ndarray) -> str:
    '''
    [CHECK_ARRAY_TYPE] inspects the contents of a given array
    and returns a string indicating the type of its elements
    '''
    if np.issubdtype(array.dtype, np.integer):
        return "int"
    elif np.issubdtype(array.dtype, np.floating):
        return "float"
    return "unsupported"


def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    '''
    [GIVE_BMI] verifies the correctness of the given input lists
    and returns an array containing the calculated BMI values
    '''
    try:
        if not height or not weight:
            raise ValueError("input list(s) cannot be empty")
        if len(height) != len(weight):
            raise ValueError("input lists are not of the same size")

        height_array = np.array(height)
        weight_array = np.array(weight)

        height_type = check_array_type(height_array)
        weight_type = check_array_type(weight_array)

        if height_type == "unsupported" or weight_type == "unsupported":
            raise TypeError("lists do not contain valid data types")
        if np.any(height_array <= 0) or np.any(weight_array <= 0):
            raise TypeError("lists do not contain valid numbers")

        bmi = weight_array / (height_array ** 2)
        return bmi.tolist()

    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    [APPLY_LIMIT] verifies the correctness of the given input
    values and returns a list of booleans
    '''
    try:
        if not bmi:
            raise ValueError("input list cannot be empty")
        if type(limit) is not int:
            raise TypeError("'limit' must be an integer")

        bmi_array = np.array(bmi)
        bmi_type = check_array_type(bmi_array)
        if bmi_type == "unsupported":
            raise TypeError("input list does not contain valid data types")
        if np.any(bmi_array <= 0):
            raise TypeError("input list does not contain valid numbers")

        above_limit = bmi_array > limit
        return above_limit.tolist()

    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
