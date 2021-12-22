# -*- coding: utf-8 -*-

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88",
                                   email="111@111.ru", id_contact=None))
    #old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    # assert len(old_contacts) == app.contact.count()
    #new_contacts = app.contact.get_contacts_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[0:1] = []
    #assert old_contacts == new_contacts
