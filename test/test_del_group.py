from model.group import Group
from random import randrange


def test_delete_some_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="group32", header="header32", footer="footer32"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

