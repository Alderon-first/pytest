# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

#инициализатор фикстуры
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.deastroy)
    return fixture


def test_add_group(app):
     app.login(password="secret", username="admin")
     app.create_group(Group(name="group", header="header", footer="footer"))
     app.logout()
