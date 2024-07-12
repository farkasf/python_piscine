import sys


def ft_calculate(num):
    if num % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")


try:
    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        ft_calculate(num)
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
except AssertionError as e:
    print(f"AssertionError: {e}")
