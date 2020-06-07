import os
from sys import argv
from array import array
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
# BUGS: PROJECT 226, doesn't fetch question 3 and 4
# BUGS:


class Hodor:
    # LOGIN AND GO TO PROJECT PAGE
    def __init__(self):
            self.driver = webdriver.Chrome()
            self.driver.get("http://158.69.76.135/level2.php")
            sleep(15)
            for i in range(0, 4096):
                self.driver.find_element_by_xpath("/html/body/form/input[1]")\
                    .send_keys('1661')
                self.driver.find_element_by_xpath("/html/body/form/input[2]")\
                    .click()
                sleep(1)
                self.driver.get("http://158.69.76.135/level2.php")
Hodor()


