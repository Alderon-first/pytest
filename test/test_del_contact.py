# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3", mobile="8-888-88-88-88",
                                   email="111@111.ru"), )
    app.contact.delete_first_contact()
