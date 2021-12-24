# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88",
                                   email="111@111.ru", id_contact=None), )
    old_groups = app.contact.get_contacts_list()
    app.contact.change_first_contact(
        Contact(firstname="Name 4", middlename="Name 5", lastname="Name 6", mobile="9-888-88-88-88", email="222@222.ru",
                id_contact=None))
    new_groups = app.contact.get_contacts_list()
    assert len(old_groups) == len(new_groups)
