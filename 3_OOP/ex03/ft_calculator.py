import sys


class calculator:
    '''
    [CALCULATOR] A class able to perform arithmetic operations.
    '''
    def __init__(self, vector: list):
        '''
        [CALCULATOR->INIT] Constructor instantiating the calculator
        with a vector.
        '''
        self._vector = vector

    def __str__(self):
        '''
        [CALCULATOR->STR] Returns a string representation of the
        stored vector.
        '''
        return str(self._vector)

    def __add__(self, object: float) -> None:
        '''
        [CALCULATOR->ADD] Overrides the '+' operator to calculate
        the sum of the vector and a scalar.
        '''
        self._vector = [num + object for num in self._vector]
        print(self._vector)

    def __mul__(self, object: float) -> None:
        '''
        [CALCULATOR->MUL] Overrides the '*' operator to calculate
        the product of the vector and a scalar.
        '''
        self._vector = [num * object for num in self._vector]
        print(self._vector)

    def __sub__(self, object: float) -> None:
        '''
        [CALCULATOR->SUB] Overrides the '-' operator to calculate
        the difference between the vector and a scalar.
        '''
        self._vector = [num - object for num in self._vector]
        print(self._vector)

    def __truediv__(self, object: float) -> None:
        '''
        [CALCULATOR->DIV] Overrides the '/' operator to calculate
        the division of the vector by a scalar. Prints an error if
        division by zero is attempted.
        '''
        if object == 0:
            print("ZeroDivisionError: Cannot divide by zero.")
            sys.exit(1)
        self._vector = [num / object for num in self._vector]
        print(self._vector)
