# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_groups = app.contact.get_contacts_list()
    app.contact.create(
        Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88", email="111@111.ru",
                id_contact=None))
    new_groups = app.contact.get_contacts_list()
    assert len(old_groups)+1 == len(new_groups)
