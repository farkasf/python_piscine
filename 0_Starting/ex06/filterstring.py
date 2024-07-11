import sys
from ft_filter import ft_filter


def check_params(argv: list) -> bool:
    '''
    [CHECK_PARAMS] Takes argument values as parameters and verifies
    their number and correct types.
    '''
    try:
        if len(argv) != 3:
            raise AssertionError("the arguments are bad")
        elif type(argv[1]) is not str:
            raise AssertionError("the arguments are bad")
        try:
            int(argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return False
    return True


def main():
    '''
    [MAIN] Calls check_params() to validate the input, then splits
    the input string (S) into words and prints those with a length
    greater than the specified integer (N).
    '''
    if not check_params(sys.argv):
        return

    splitted = sys.argv[1].split()
    filtered = ft_filter(lambda x: len(x) > int(sys.argv[2]), splitted)
    print(list(filtered))


if __name__ == "__main__":
    main()
