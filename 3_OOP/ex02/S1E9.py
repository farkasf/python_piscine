from abc import ABC, abstractmethod


class Character(ABC):
    '''
    [CHARACTER] An abstract class containing first name
    and health status as attributes.
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        [CHARACTER->INIT] Constructor instantiating Character
        with 2 instance variables first_name and is_alive.
        '''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''
        [CHARACTER->DIE] Abstract method to change the is_alive attribute.
        '''
        pass


class Stark(Character):
    '''
    [STARK] A subclass of Character representing
    a member of the Stark family. Includes a method die().
    '''
    def die(self):
        '''
        [STARK->DIE] A method changing is_alive to False.
        '''
        self.is_alive = False
