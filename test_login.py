import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.base_url = "http://localhost/"
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get(driver.base_url + "litecart/admin/login.php")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[16]").click()
    driver.find_element_by_link_text("Create New User").click()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("Manola")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("545")
    driver.find_element_by_name("confirmed_password").clear()
    driver.find_element_by_name("confirmed_password").send_keys("545")
    driver.find_element_by_name("save").click()
    driver.find_element_by_xpath("//td[@id='sidebar']/div[2]/a[5]/i").click()

# def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True
#
# def is_alert_present(self):
#         try:
#             self.driver.switch_to_alert()
#         except NoAlertPresentException as e:
#             return False
#         return True

   # def close_alert_and_get_its_text(self):
   #     try:
   #         alert = self.driver.switch_to_alert()
   #         alert_text = alert.text
   #         if self.accept_next_alert:
   #             alert.accept()
   #         else:
   #             alert.dismiss()
   #         return alert_text
   #     finally:
   #         self.accept_next_alert = True

# def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
#
#
# if __name__ == "__main__":
#     unittest.main()

#class MyTestCase(unittest.TestCase):
#    def test_something(self):
#        self.assertEqual(True, False)


#if __name__ == '__main__':
#    unittest.main()
