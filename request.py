import datetime


class Request:
    def __init__(self):
        self.__request_ID = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")

    # Admin entering request - pulled from user logged into the system
    # User making request - manual entry
    # Request description - short description
    # Resolution - Drop-down item list: Open, Approve, Deny, Defer
    # Notes - Large textbox for information about resolution

    # def __str__(self):
    #     return '{}'.format(self.__name)
    #
    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, name):
    #     self.__name = name
