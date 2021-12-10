# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(password="secret", username="admin")
    app.group.create(Group(name="group", header="header", footer="footer"))
    app.session.logout()