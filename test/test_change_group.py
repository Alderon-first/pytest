# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random


def test_change_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group32", header="header32", footer="footer32"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    # group.id_group = old_groups[index].id_group
    # тут сохраняем id группы, которую будем менять
    app.group.modify_group_by_id(group.id_group, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    # old_groups[id] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
