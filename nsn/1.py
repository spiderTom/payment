#coding:utf-8
import unittest
import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url_login = "http://www.nsntradeunion.com.cn/bbs/mvnforum/login"
        self.url_chinese = "https://www.excelityglobal.cn/embrace/jsp/index.jsp?locale=zhCN"
        self.url_query = "https://www.excelityglobal.cn/embrace/servlet/controller?module=Payroll&screen=PayslipSelfServiceCN&action=Query"


    def capturePicture(self):
        self.driver.execute_script("""
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
            if "scroll-done" in self.driver.title:
                break
            self.driver.implicitly_wait(10)

        self.driver.save_screenshot("capture1.png")


    def saveHtml(self, fileName):
        f = open(fileName, 'w+')
        f.write(self.driver.page_source.encode('utf-8'))
        f.close()

    def test_search_in_python_org(self):
        conf=ConfigParser.ConfigParser()
        conf.readfp(open("config.ini", "rb"))
        print conf.get("wujia", "ID")
        print conf.get("wujia", "PASSWORD")

        driver = self.driver
        driver.get(self.url_login)
        print driver.title
        elem = driver.find_element_by_name("MemberName")
        elem.send_keys("61463034")
        elem = driver.find_element_by_name("MemberMatkhau")
        elem.send_keys("123456")
        elem.send_keys(Keys.RETURN)
        #login finished
        print driver.title
        print driver.page_source
        #driver.get(self.url_query)
        #txtStartDate

        #print driver.page_source
        self.saveHtml("111.html")
        self.capturePicture()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
