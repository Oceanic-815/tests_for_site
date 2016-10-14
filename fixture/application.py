from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
#from fixture.session_cont import Session_contHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self) # for contacts
        #self.session_cont = Session_contHelper(self) # for contacts

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
"""
class Actions:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.contact = ContactHelper(self)
        self.session_cont = Session_contHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
"""