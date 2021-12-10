# -*- coding: utf-8 -*-
from model.group import Group


def test_change_first_group(app):
    app.session.login(password="secret", username="admin")
    app.group.change_first_group(Group(name="group1", header="header1", footer="footer1"))
    app.session.logout()

