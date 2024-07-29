from typing import Any


def sort_nums(nums: tuple) -> list:
    '''
    [SORT_NUMS] Accepts a tuple with the input numbers, sorts
    them using a bubble sort algorithm and returns a list.
    '''
    size = len(nums)
    content = list(nums)
    for i in range(size):
        for j in range(size - i - 1):
            if content[j] > content[j + 1]:
                temp = content[j]
                content[j] = content[j + 1]
                content[j + 1] = temp
    return content


def get_mean(nums: list) -> float:
    '''
    [GET_MEAN] Calculates the mean of a list of numbers.
    '''
    mean = sum(nums) / len(nums)
    return mean


def get_median(nums: list) -> float:
    '''
    [GET_MEAN] Calculates the median of a list of numbers.
    '''
    size = len(nums)
    middle = size // 2
    if size % 2 == 1:
        median = nums[middle]
    else:
        median = (nums[middle] + nums[middle - 1]) / 2
    return median


def get_quartile(nums: list) -> list:
    '''
    [GET_QUARTILE] Calculates the quartile q1 (25%) and q3
    (75%) of a list of numbers.
    '''
    size = len(nums)
    middle = size // 2
    q3 = get_median(nums[middle:])
    if size % 2 == 1:
        q1 = get_median(nums[:middle + 1])
    else:
        q1 = get_median(nums[:middle])
    return [float(q1), float(q3)]


def get_variance(nums: list) -> float:
    '''
    [GET_VARIANCE] Calculates the variance (average squared
    deviation from the mean) of a list of numbers.
    '''
    mean = get_mean(nums)
    deviations = []
    for num in nums:
        deviations.append((num - mean) ** 2)
    sigma_sq = get_mean(deviations)
    return sigma_sq


def get_std(nums: list) -> float:
    '''
    [GET_STD] Calculates the standard deviation (the square
    root of the variance).
    '''
    sigma_sq = get_variance(nums)
    std = sigma_sq ** 0.5
    return std


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''
    [FT_STATISTICS] Performs various statistical calculations
    (mean, median, quartile, standard deviation, variance) based
    on provided numbers and requested operations. The input tuple
    is sorted prior to calculations. Includes error handling for
    issues related to data types and argument contents.
    '''
    ops_menu = {
        "mean": get_mean,
        "median": get_median,
        "quartile": get_quartile,
        "std": get_std,
        "var": get_variance
    }

    for arg in args:
        if not isinstance(arg, (int, float)):
            print("TypeError: Arguments must be numbers.")
            return

    nums = sort_nums(args)

    for ops in kwargs.values():
        if len(nums) == 0:
            print("ERROR")
        elif ops in ops_menu:
            print(f"{ops} : {ops_menu[ops](nums)}")
