from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # open groups page
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_telephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_contact_page()
        self.contacts_cache = None

    def change_first_contact(self):
        wd = self.app.wd
        # ?????????????? ????????????
        self.select_contact_by_index(0)
        self.contacts_cache = None

    def change_contact_by_index(self, index, contact):
        wd = self.app.wd
        # ?????????????? ????????????
        self.open_home_page()
        self.open_contact_by_index(index)
        # ???????????????? ??????????????????
        # wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_contact_page()
        self.contacts_cache = None


    def change_contact_by_id(self, id_contact, contact):
        wd = self.app.wd
        # ?????????????? ????????????
        self.open_home_page()
        self.open_contact_by_id(id_contact)
        # ???????????????? ??????????????????
        # wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_contact_page()
        self.contacts_cache = None

    def open_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        # wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_by_id(self, id_contact):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[id]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        # wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # ?????????????? ????????????
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.return_contact_page()
        self.contacts_cache = None

    def delete_contact_by_id(self, id_contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id_contact)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.return_contact_page()
        self.contacts_cache = None

    def select_contact_by_id(self, id_contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id_contact).click()

    def delete_first_contact(self):
        wd = self.app.wd
        # ?????????????? ????????????
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        # ?????????????? ???????????? ????????????
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.return_contact_page()
        self.contacts_cache = None

    def move_first_contact_to_first_group(self):
        self.add_contact_to_group_by_index(0)

    def change_select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def add_contact_to_group_by_index(self, contact_index, group_for_add):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector(f"input[id='{contact_index}']").click()
        self.change_select_field_value("to_group", group_for_add)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text(f'group page "{group_for_add}"').click()

    def delete_contact_from_group_by_index(self, contact_index, delete_from_group):
        wd = self.app.wd
        self.change_select_field_value("group", delete_from_group)
        wd.find_element_by_css_selector(f"input[id='{contact_index}']").click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text(f'group page "{delete_from_group}"').click()

    def move_contact_to_group_by_id(self, id_contact, id_group):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id_contact)
        # select group
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(id_group)
        # submit add
        wd.find_element_by_name("add").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def return_contact_page(self):
        wd = self.app.wd
        # return contact page
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_elements_by_css_selector("td")[1].text
                firstname = element.find_elements_by_css_selector("td")[2].text
                address = element.find_elements_by_css_selector("td")[3].text
                all_emails = element.find_elements_by_css_selector("td")[4].text
                id_contact = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_elements_by_css_selector("td")[5].text
                self.contacts_cache.append(Contact(firstname=firstname, middlename=None, lastname=lastname,
                                                   address=address, id_contact=id_contact,
                                                   all_emails_from_home_page=all_emails,
                                                   all_phones_from_home_page=all_phones))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        id_contact = wd.find_element_by_name("id").get_attribute('value')
        address = wd.find_element_by_name("address").text.strip()
        email = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute('value')
        # fax = wd.find_element_by_name("mobile").get_attribute('value')
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id_contact=id_contact, address=address,
                       email=email, email2=email2, email3=email3,
                       home_telephone=home_telephone, mobile=mobile,
                       work_telephone=work_telephone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        mobile = re.search("M: (.*)", text).group(1)
        home_telephone = re.search("H: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(firstname=None, lastname=None, id_contact=None, mobile=mobile,
                       email=None, middlename=None, home_telephone=home_telephone, work_telephone=work_telephone,
                       phone2=phone2)
