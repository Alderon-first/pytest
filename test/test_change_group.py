# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_change_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group32", header="header32", footer="footer32"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="group1", header="header1", footer="footer1")
    group.id_group = old_groups[index].id_group
    # тут сохраняем id группы, которую будем менять
    app.group.change_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
