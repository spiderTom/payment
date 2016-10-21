import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.excelityglobal.cn/embrace/servlet/login")
        self.assertIn("HRWorkways", driver.title)
        print driver.title
        elem = driver.find_element_by_name("usrCorporation")
        elem.send_keys("nsn")
        elem = driver.find_element_by_name("usrLoginId")
        elem.send_keys("61463034")
        elem = driver.find_element_by_name("usrPassword")
        elem.send_keys("AAAsss11")
        driver.find_element_by_id("usrPassword").send_keys(Keys.RETURN)

    def tearDown(self):
        i = 11
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()