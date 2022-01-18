# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import testdata


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])
def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    # contact = Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3",
                      # mobile="8-888-88-88-88", work_telephone="123-456", home_telephone="2364566",
                      # email="111@111.ru", email2="222@222.ru", address="ул ленина", id_contact=None)
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
