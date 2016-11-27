import pytest
from selenium import webdriver


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

