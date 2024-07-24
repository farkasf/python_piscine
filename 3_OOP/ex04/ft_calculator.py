class calculator:
    '''
    [CALCULATOR] A class able to perform vector calculations.
    '''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''
        [CALCULATOR->DOT_PRODUCT] Calculates the scalar product
        of two vectors:
        (x1, y1) * (x2, y2) = x1 * x2 + y1 * y2
        '''
        result = sum(V1[i] * V2[i] for i in range(len(V1)))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''
        [CALCULATOR->ADD_VEC] Performs vector addition:
        (x1, y1) + (x2, y2) = (x1 + x2, y1 + y2)
        '''
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''
        [CALCULATOR->SUB_VEC] Performs vector subtraction:
        (x1, y1) - (x2, y2) = (x1 - x2, y1 - y2)
        '''
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {result}")
