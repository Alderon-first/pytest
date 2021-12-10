# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    app.session.login(password="secret", username="admin")
    app.contact.delete_first_contact()
    app.session.logout()

