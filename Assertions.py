"""
Assertion is nothing but the check point or you can say it as
verification for the test case to evaluate some item on the execution.

If we don't provide any assertion inside a test case then
there is no way to know whether a test case is failed or not.

Assertion helps in report generation, based on the
assertions the test execution report will generate.

there are few assertions which will accept all the values
and few assertions will accept only numeric values.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.firefox import service


# service = service.Service(executable_path=r'C:\Users\jojo\Drivers\geckodriver-v0.26.0-win64\geckodriver')
# service.start()
# capabilities = {'firefox.binary': "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"}
# driver = webdriver.Remote(service.service_url, capabilities)


class Test(unittest.TestCase):

    def testname(self):
        #self.assertGreater(100,10)
        self.assertGreaterEqual(5,5)
        self.assertLess(8,9)
        self.assertLessEqual()
        list = {"python", "selenium", "java"}
        #self.assertIn("python", list)
        #self.assertNotIn("ruby", list)
        #self.assertIsNone(driver)
        #self.assertIsNotNone(driver)
        # driver.get("https://www.google.com/")
        # titleofwebpage = driver.title

        #self.assertEqual("Google", titleofwebpage, "webpage title is not same")
        #self.assertNotEqual("Google123", titleofwebpage)

        # self.assertTrue(titleofwebpage == "Google")
        # self.assertFalse(titleofwebpage == "Google123")


if __name__ == "__main__":
        unittest.main()
