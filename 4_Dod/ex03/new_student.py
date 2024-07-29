import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''
    [GENERATE_ID] Generates a random ID string.
    '''
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    '''
    [GENERATE_LOGIN] Generates a login string using
    an uppercase name initial and surname in lowercase.
    '''
    return (name[:1].capitalize() + surname.lower())


@dataclass
class Student:
    '''
    [STUDENT] A dataclass containing student info:
    - name and surname are set upon construction
    - active is set to True by default
    - login and id are automatically generated and
      are not initializable
    '''
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        '''
        [POST_INIT] Initializes the student login
        after the object has been created.
        '''
        self.login = generate_login(self.name, self.surname)
