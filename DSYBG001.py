import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.excelityglobal.cn/embrace/servlet/login")
        self.assertIn("HRWorkways", driver.title)

        driver.get("https://www.excelityglobal.cn/embrace/jsp/index.jsp?locale=zhCN")
        print driver.title
        elem = driver.find_element_by_name("usrCorporation")
        elem.send_keys("nsn")
        elem = driver.find_element_by_name("usrLoginId")
        elem.send_keys("61463034")
        elem = driver.find_element_by_name("usrPassword")
        elem.send_keys("AAAsss11")
        driver.find_element_by_id("usrPassword").send_keys(Keys.RETURN)
        #login finished
        driver.get("https://www.excelityglobal.cn/embrace/servlet/controller?module=Payroll&screen=PayslipSelfServiceCN&action=Query")
        #txtStartDate
        elem = driver.find_element_by_name("txtStartDate")
        driver.find_element_by_xpath("//option[@value='2016/8']").click()

        driver.find_element_by_xpath("//input[@type='button']").send_keys(Keys.RETURN)
        #driver.find_elements(By.XPATH, '//button[1]').send_keys(Keys.RETURN)
        #driver.find_element_by_class_name("button").send_keys(Keys.RETURN)

    def tearDown(self):
        i = 11
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()