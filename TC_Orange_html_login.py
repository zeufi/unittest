import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.firefox import service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Orangetest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path= r'C:\Users\jojo\Drivers\geckodriver-v0.26.0-win64\geckodriver.exe')
        cls.driver.maximize_window()

    def test_homepagetitle(self):
        self.driver.get("http://newtours.demoaut.com/")
        self.assertEqual("Welcome: Mercury Tours", self.driver.title, "webpage title is not matching")

    def test_login(self):
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("mercury")
        self.driver.find_element_by_name("login").click()
        self.assertEqual("Welcome: Mercury Tours", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\jojo\PycharmProjects\Seleniumproject\UnitTest"))


"""
To run the test via terminal:
1.
path where is the file>python -m unittest TC_Orang
e_html_login

2. To generate html logs
path where is the file>python TC_Orang
e_html_login.py
 
"""