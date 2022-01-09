# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3",
                      mobile="8-888-88-88-88", email="111@111.ru", id_contact=None)
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
