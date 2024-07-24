from S1E9 import Character


class Baratheon(Character):
    '''
    [BARATHEON] Representing the Baratheon family.
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        [BARATHEON->INIT] Constructor instantiating Character
        with 3 extra instance variables family_name, eyes and hairs.
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        '''
        [BARATHEON->STR] Returns a string representation of the object.
        '''
        return self.__repr__()

    def __repr__(self):
        '''
        [BARATHEON->REPR] Provides a detailed string representation of
        the object.
        '''
        info = f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return info

    def die(self):
        '''
        [BARATHEON->DIE] A method changing is_alive to False.
        '''
        self.is_alive = False


class Lannister(Character):
    '''
    [LANNISTER] Representing the Lannister family.
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        [LANNISTER->INIT] Constructor instantiating Character
        with 3 extra instance variables family_name, eyes and hairs.
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''
        [LANNISTER->DIE] A method changing is_alive to False.
        '''
        self.is_alive = False

    def __str__(self):
        '''
        [LANNISTER->STR] Returns a string representation of the object.
        '''
        return self.__repr__()

    def __repr__(self):
        '''
        [LANNISTER->REPR] Provides a detailed string representation of
        the object.
        '''
        info = f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return info

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        '''
        [LANNISTER->CREATE_LANNISTER] Creates a new Lannister character.
        Can be called directly on the class without creating an
        instance of it first.
        '''
        return cls(first_name, is_alive)
