# -*- coding: utf-8 -*-
from model.group import Group


def test_change_first_group(app):
    if app.contact.count() == 0:
        app.contact.create(Group(name="group32", header="header32", footer="footer32"))
    app.group.change_first_group(Group(name="group1", header="header1", footer="footer1"))
