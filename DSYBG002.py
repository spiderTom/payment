#coding:utf-8
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
        #print driver.page_source
        #f = open('001.html', 'w+')
        #f.write(driver.page_source)
        #f.close()
        #driver.set_window_size(1200, 900)
        #driver.save_screenshot("codingpy.png")
        driver.execute_script("""
            (function () {
                var y = 0;
                var step = 100;
                window.scroll(0, 0);

                function f() {
                    if (y < document.body.scrollHeight) {
                        y += step;
                        window.scroll(0, y);
                        setTimeout(f, 100);
                    } else {
                        window.scroll(0, 0);
                        document.title += "scroll-done";
                    }
                }

                setTimeout(f, 1000);
            })();
        """)

        for i in xrange(30):
            if "scroll-done" in driver.title:
                break
            self.driver.implicitly_wait(10)

        driver.save_screenshot("capture1.png")


    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()