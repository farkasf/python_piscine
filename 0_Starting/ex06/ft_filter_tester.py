from ft_filter import ft_filter

BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
DEF = "\033[0m"

numbers = [1, -2, -3, 4, -5, 6, -7, 8, 9]
characters = ('a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J')
words = ["hello", "world", "and", "hi", "there", "Marvin"]


def run_test(no, testName, function, iterable):
    print(f"{YELLOW}TEST {no}: {testName}{DEF}")
    ft_test = ft_filter(function, iterable)
    sys_test = filter(function, iterable)
    ft_test_list = list(ft_test)
    sys_test_list = list(sys_test)
    print(f"ft_filter: {ft_test_list} | filter: {sys_test_list}")
    if sys_test_list != ft_test_list:
        print(f"{RED}diff ko{DEF}")
    else:
        print(f"{GREEN}diff ok{DEF}")


def numbers_set():
    print(f"{BLUE}using sequence\n{list(numbers)}{DEF}\n")
    run_test(1, "no function passed", None, numbers)
    run_test(2, "negative numbers", lambda x: x > 0, numbers)
    run_test(3, "odd numbers", lambda x: x % 2 != 0, numbers)
    run_test(4, "power of 2", lambda x: (x & (x - 1)) == 0, numbers)
    run_test(5, "greater than 10", lambda x: x > 10, numbers)


def char_set():
    print(f"\n{BLUE}using sequences\n{list(characters)}\n{list(words)}{DEF}\n")
    run_test(6, "uppercase letters", lambda x: 'Z' >= x >= 'A', characters)
    run_test(7, "lowercase letters", lambda x: 'z' >= x >= 'a', characters)
    run_test(8, "words containing 'e'", lambda x: 'e' in x, words)
    run_test(9, "words of length greater than 5", lambda x: len(x) > 5, words)
    run_test(10, "words equal to '42'", lambda x: x == 42, words)


if __name__ == "__main__":
    numbers_set()
    char_set()
    print(f"\n{BLUE}10/10 done{DEF}")
