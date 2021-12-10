# импорт библиотеки
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application():  # инструкция по созданию пищеварительной системы(апликейшен), которая содержит инструкцию о создании почки (менеджер)
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        # open home page
        wd = self.wd  # вызов  WebDriver, извлечение ссылки на драйвер из текущего объета
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
