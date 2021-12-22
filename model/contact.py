class Contact:
    def __init__(self, firstname, middlename, lastname, mobile, email, id_contact):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.mobile = mobile
        self.email = email
        self.id_contact = id_contact

    def __repr__(self):
        return "%s:%s:%s" % (self.firstname, self.lastname, self.id_contact)
        # это про вывод информации на консоль

    def __eq__(self, other):
        return self.id_contact == other.id_contact \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname
        # это про логическое сравнение параметров (чтобы сравнивалось значение, а не значение+расположение информации)

