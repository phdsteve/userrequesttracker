class User:

    def __init__(self, name):
        self.__name = name
        self.is_admin = False

    def __str__(self):
        return '{}'.format(self.__name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.is_admin = True
