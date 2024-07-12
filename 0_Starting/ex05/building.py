import sys


def count_char(input_data: str):
    '''
    [COUNT_CHAR] takes a string as a parameter and counts and categorizes
    characters in it, then prints the count for each category (uppercase
    letters, lowercase letters, punctuation marks, spaces and digits)
    '''
    storage = {
        "uCase": 0,
        "lCase": 0,
        "space": 0,
        "digit": 0,
        "punc": 0
    }

    for c in input_data:
        if ord(c) < 32 or ord(c) > 126:
            continue
        elif 'Z' >= c >= 'A':
            storage["uCase"] += 1
        elif 'z' >= c >= 'a':
            storage["lCase"] += 1
        elif c.isspace():
            storage["space"] += 1
        elif c.isdigit():
            storage["digit"] += 1
        else:
            storage["punc"] += 1

    print(f"The text contains {sum(storage.values())} characters:")
    print(f"{storage['uCase']} upper letters")
    print(f"{storage['lCase']} lower letters")
    print(f"{storage['punc']} punctuation marks")
    print(f"{storage['space']} spaces")
    print(f"{storage['digit']} digits")


def main():
    '''
    [MAIN] processes input for character counting - checks for an argument
    or prompts the user to enter a string, raises an error for empty input
    or multiple arguments - calls count_char() to count characters
    '''
    try:
        if len(sys.argv) == 1 or not sys.argv[1]:
            try:
                str_to_count = input("What is the text to count?\n")
                if not str_to_count:
                    raise AssertionError("entered an empty string")
            except EOFError:
                raise AssertionError("entered an empty string")
        elif len(sys.argv) == 2:
            str_to_count = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        count_char(str_to_count)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
