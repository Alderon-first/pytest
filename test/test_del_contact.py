# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_del_some_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88",
                                   email="111@111.ru", id_contact=None))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
