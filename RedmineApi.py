import redminelib as rdm


class RedmineApi:
    """класс взаимодейтсвия с Redmine"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(RedmineApi, cls).__new__(cls)
        return cls.__instance

    def __init__(self, error_text):
        self.__site = "http://192.168.0.21/redmine/"
        self.redmine = None
        self.connection = False
        self.error_text = error_text

    def connecting(self, __login, __password):
        """функция подключения к Redmine"""
        try:
            self.redmine = rdm.Redmine(self.__site, username=__login, password=__password)
            self.connection = True
        except Exception as e:
            print(e)
            self.error_text.set("Ошибка подключения к серверу")

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
