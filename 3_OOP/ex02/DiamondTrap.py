from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''
    [KING] Representing the king family. Inherits from both
    Baratheon and Lannister.
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        [KING->INIT] Constructor instantiating King
        with 2 instance variables first_name and is_alive.
        '''
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        '''
        [KING->GET_EYES] Gets the color of the eyes.
        '''
        return self.eyes

    def set_eyes(self, colour):
        '''
        [KING->SET_EYES] Sets the color of the eyes.
        '''
        self.eyes = colour

    def get_hairs(self):
        '''
        [KING->GET_HAIRS] Gets the color of the hairs.
        '''
        return self.hairs

    def set_hairs(self, colour):
        '''
        [KING->SET_HAIRS] Sets the color of the hairs.
        '''
        self.hairs = colour
