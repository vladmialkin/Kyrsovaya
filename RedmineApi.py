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
        self.redmine = None
        self.connection = False
        self.error_text = error_text

    def connecting(self, __login, __password):
        """функция подключения к Redmine"""
        try:
            self.redmine = rdm.Redmine(self.__site, username=__login, password=password)
            self.connection = True
        except:
            self.error_text.set("Неверно введен логин/пароль")

    def get_projects_all(self):
        """функция получает объект всех проектов"""
        return self.redmine.project.all(limit=1000)

    def get_trackers_all(self):
        """функция получает объект всех трекеров"""
        return self.redmine.tracker.all(limit=1000)

    def get_issues_all(self):
        """функция получает объект всех задач"""
        return self.redmine.issue.all(limit=1000)

    def get_users_all(self):
        """функция получает объект всех пользователей"""
        return self.redmine.user.all(limit=1000)
