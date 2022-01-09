# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numb(prefix, maxlen):
    symbols = string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="",
                    mobile="", work_telephone="", home_telephone="",
                    email="", email2="", address="", id_contact=None)]+[
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), mobile=random_numb("", 10), work_telephone=random_numb("", 10),
            home_telephone=random_numb("", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            address=random_string("address", 10), id_contact=None)
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    # contact = Contact(firstname="Name 1", middlename="Name 2", lastname="Name 3",
                      # mobile="8-888-88-88-88", work_telephone="123-456", home_telephone="2364566",
                      # email="111@111.ru", email2="222@222.ru", address="ул ленина", id_contact=None)
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
