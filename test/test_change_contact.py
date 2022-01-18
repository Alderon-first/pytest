# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_change_some_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88",
                                   email="111@111.ru", id_contact=None))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Name 4", middlename="Name 5", lastname="Name 6",
                      mobile="9-888-88-88-88", email="222@222.ru", id_contact=None)
    contact.id_contact = old_contacts[index].id_contact
    app.contact.change_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

