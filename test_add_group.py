# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        # open home page
        wd = self.wd #вызов  WebDriver, извлечение ссылки на драйвер из текущего объета
        wd.get("http://localhost/addressbook/")

    def login(self, password, username):
        # Login
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        # open groups page
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill groups +
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def return_to_groups_page(self):
        # return groups page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        # Logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def test_add_group(self):
        self.login(password="secret", username="admin")
        self.create_group(Group(name="group", header="header", footer="footer"))
        self.logout()



    #def is_element_present(self, how, what):
    #    try: self.wd.find_element(by=how, value=what)
    #    except NoSuchElementException as e: return False
    #    return True
    
    #def is_alert_present(self):
    #    try: self.wd.switch_to_alert()
    #    except NoAlertPresentException as e: return False
    #    return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
