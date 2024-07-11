import sys


def to_morse(msg: str) -> str:
    '''
    [TO_MORSE] Converts the string passed as a parameter into
    Morse code, raising an error if an alphanumeric character
    is not found in the given dictionary of alphabet keys.
    '''
    NESTED_MORSE = {
        " ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-",
        "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
        "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", "0": "-----"
    }
    output = ""
    try:
        for char in msg:
            if char.upper() in NESTED_MORSE:
                output += f"{NESTED_MORSE[char.upper()]} "
            else:
                raise AssertionError
    except AssertionError:
        print("AssertionError: unsupported characters found")
        return None
    return output.rstrip()


def check_params(argv: list) -> bool:
    '''
    [CHECK_PARAMS] Takes argument values as parameters and verifies
    their number and correct types.
    '''
    try:
        if len(argv) != 2:
            raise AssertionError
        elif not argv[1] or type(argv[1]) is not str:
            raise AssertionError
        for char in argv[1]:
            if not char.isalnum() and char != ' ':
                raise AssertionError
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return False
    return True


def main():
    '''
    [MAIN] Calls check_params() to validate the input, then encodes
    the input string into Morse code and prints the encoded result.
    '''
    if not check_params(sys.argv):
        return
    encoded = to_morse(sys.argv[1])
    if encoded:
        print(encoded)


if __name__ == "__main__":
    main()
