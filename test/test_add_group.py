# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.groups import testdata


# @pytest.mark.parametrize("group", testdata, ids=[repr(x)for x in testdata])
def test_add_group(app, data_groups):
    group = data_groups
    # pass
    old_groups = app.group.get_group_list()
    # group = Group(name="group", header="header", footer="footer")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
