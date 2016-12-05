#coding:utf-8
import unittest
import ConfigParser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url_login = "https://www.excelityglobal.cn/embrace/servlet/login"
        self.url_chinese = "https://www.excelityglobal.cn/embrace/jsp/index.jsp?locale=zhCN"
        self.url_query = "https://www.excelityglobal.cn/embrace/servlet/controller?module=Payroll&screen=PayslipSelfServiceCN&action=Query"
        conf=ConfigParser.ConfigParser()
        conf.readfp(open("config.ini", "rb"))
        self.ID = conf.get("user", "ID")
        self.password = conf.get("user", "PASSWORD")
        time.localtime(time.time())

        self.m_year = time.strftime('%Y',time.localtime(time.time()))
        self.m_month = time.strftime('%m',time.localtime(time.time()))
        self.m_day = time.strftime('%d',time.localtime(time.time()))
        self.options = self.m_year + "/" + self.m_month


    def getOptions(self):
        day = (int)(self.m_day)
        month = (int)(self.m_month)
        if day <= 24:
            self.m_month = str(month - 1)
        self.options = self.m_year + "/" + self.m_month

    def getFileName(self):
        day = (int)(self.m_day)
        month = (int)(self.m_month)
        if day <= 24:
            self.m_month = str(month - 1)
        self.filename = self.m_year + "_" + self.m_month + ".html"

    def capturePicture(self, picturename):
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

        self.driver.save_screenshot(picturename)


    def saveHtml(self, fileName):
        f = open(fileName, 'w+')
        f.write(self.driver.page_source.encode('utf-8'))
        f.close()

    def test_get_my_pay(self):
        driver = self.driver
        driver.get(self.url_login)
        driver.get(self.url_chinese)
        print driver.title
        elem = driver.find_element_by_name("usrCorporation")
        elem.send_keys("nsn")
        elem = driver.find_element_by_name("usrLoginId")
        elem.send_keys(self.ID)
        elem = driver.find_element_by_name("usrPassword")
        elem.send_keys(self.password)
        driver.find_element_by_id("usrPassword").send_keys(Keys.RETURN)
        #login finished
        driver.get(self.url_query)
        elem = driver.find_element_by_name("txtStartDate")

        self.getOptions()
        result = "//option[@value='" + self.options + "']"
        driver.find_element_by_xpath(result).click()

        driver.find_element_by_xpath("//input[@type='button']").send_keys(Keys.RETURN)

        #print driver.page_source
        htmlname = str(self.options)
        htmlname = htmlname.replace('/','_')
        picturename = htmlname
        htmlname += ".html"
        picturename += ".png"
        print htmlname
        self.saveHtml(htmlname)
        self.capturePicture(picturename)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
