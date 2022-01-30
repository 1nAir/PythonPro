class Human:
    """
    Human params
    """
    def __init__(self, name: str, surname: str, age: int):
        """

        :param name:
        :param surname:
        :param age:
        """
        if isinstance(name, str) and isinstance(surname, str) and isinstance(age, int):
            self.name = name
            self.surname = surname
            self.age = age
        else:
            raise TypeError('Invalid params')
