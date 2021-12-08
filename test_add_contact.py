# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from contact import Contact
from application import Application


#инициализатор фикстуры
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.deastroy)
    return fixture


def test_add_contact(app):
    app.login(password="secret", username="admin")
    app.creat_contact(Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88",
                      email="111@111.ru"))
    app.logout()

