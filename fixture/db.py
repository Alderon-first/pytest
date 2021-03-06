import pymysql.cursors
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(name=name, header=header, footer=footer, id_group=str(id)))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT id, firstname, middlename, lastname, nickname, company, title, address, home, 
            mobile, work, fax, email, email2, email3, homepage, 
            bday, bmonth, byear, aday, amonth, ayear, address2, phone2 
            FROM addressbook 
            WHERE deprecated ='0000-00-00 00:00:00'""")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company,
                 title, address, homephone, mobilephone, workphone, faxphone, email, email2,
                 email3, homepage, bday, bmonth, byear, aday, amonth,
                 ayear, address2, phone2) = row
                contact_list.append(Contact(id_contact=str(id), firstname=firstname, middlename=middlename,
                                            lastname=lastname, company=company,
                                            address=address, home_telephone=homephone,
                                            mobile=mobilephone, work_telephone=workphone, phone2=phone2,
                                            fax=faxphone, email=email,
                                            email2=email2, email3=email3,
                                            all_phones_from_home_page=homephone+mobilephone+workphone+phone2,
                                            all_emails_from_home_page=email+email2+email3))
        finally:
            cursor.close()
        return contact_list

    def get_all_contacts_not_in_groups(self):
        contact_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("""select 
                                      a.id, a.firstname
                                 from addressbook a left join address_in_groups ag
                                 on a.id = ag.id
                                 left join group_list g
                                 on ag.group_id = g.group_id  
                                 where a.deprecated = '0000-00-00 00:00:00'
                                 and ag.group_id is NULL  """)
            for row in cursor:
                (id_contact, firstname) = row
                contact_list.append(Contact(id_contact=id_contact))
        return contact_list

    def destroy(self):
        self.connection.close()
