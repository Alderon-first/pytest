# импорт библиотеки
from fixture.manager import Manager


class Application(
    Manager):  # инструкция по созданию пищеварительной системы(апликейшен), которая содержит инструкцию о создании почки (менеджер)

    def open_home_page(self):
        # open home page
        wd = self.wd  # вызов  WebDriver, извлечение ссылки на драйвер из текущего объета
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
