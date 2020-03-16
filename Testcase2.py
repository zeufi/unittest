import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):

    def test_Bing(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\jojo\Drivers\geckodriver-v0.26.0-win64\geckodriver')
        self.driver.get("https://bing.com")
        print("Title of the page is :" + self.driver.title)
        # self.driver.close()
        self.driver.get("http://newtours.demoaut.com/mercurywelcome.php")
        print("Title of the page is :" + self.driver.title)
        #self.driver.close()


    # def test_Google(self):
    #     self.driver = webdriver.Firefox(executable_path=r'C:\Users\jojo\Drivers\geckodriver-v0.26.0-win64\geckodriver')
    #     self.driver.get("http://newtours.demoaut.com/mercurywelcome.php")
    #     print("Title of the page is :" + self.driver.title)
    #     self.driver.close()


if __name__ == "__main__":
    unittest.main()
