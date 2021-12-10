# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact(app):
    app.contact.change_first_contact(Contact(firstname="Name 4", middlename="Name 5",
                                             lastname="Name 6", mobile="9-888-88-88-88", email="222@222.ru"))
