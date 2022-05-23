import redminelib as rdm


class RedmineApi:
    """класс взаимодейтсвия с Redmine"""
    __inctance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inctance is None:
            cls.__inctance= super(RedmineApi, cls).__new__(cls)
        return cls.__inctance

    def __init__(self, error_text):
        self.__site = None
        self.__redmine = None
        self.connection = False
        self.error_text = error_text
