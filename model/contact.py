from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_telephone=None, mobile=None, work_telephone=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, address2=None, phone2=None, id_contact=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile = mobile
        self.work_telephone = work_telephone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.id_contact = id_contact
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.firstname, self.lastname, self.id_contact)
        # это про вывод информации на консоль

    def __eq__(self, other):
        return (self.id_contact is None or other.id_contact is None or self.id_contact == other.id_contact) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname
        # это про логическое сравнение параметров (чтобы сравнивалось значение, а не значение+расположение информации)

    # если у контакта есть id, возвращаем его, если нет - возвращаем максимальное число.
    # этот метод нужен для правильной сортировки

    def id_or_max(self):
        if self.id_contact:
            return int(self.id_contact)
        else:
            return maxsize
