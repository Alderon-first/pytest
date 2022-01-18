import random

from model.group import Group
from random import randrange
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group32", header="header32", footer="footer32"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id_group)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups

