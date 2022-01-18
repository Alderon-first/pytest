# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import testdata


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    # contact = Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol ", nickname="writer", title="Title",
                    # company="Writer Union", address="Dikanka, 8 - 13", home_telephone="+31278963215",
                    # mobile="8(921)4567893", work_telephone="84958963214",
                    # fax="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com",
                    # email3="gogol3@pochta.com",
                    # homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    # aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77",
                    # phone2="89996132578")
    app.contact.create(contact)
    # assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max)
