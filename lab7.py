import unittest
import time
timestr = time.strftime("%y%m%d-%H%M%S")
from selenium import webdriver

class TestCount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")  # Store the webdriver in a particular path and call it within the program
        self.driver.get("E:\stp\democount.html")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.save_screenshot('E:\stp\screenshots\ss1.png')
        self.driver.save_screenshot("Details.png")
    def test_Countelements(self):
        textboxes = self.driver.find_elements_by_id("User input")
        print("The count of TextBoxes = ",len(textboxes))
        self.driver.save_screenshot('E:\stp\screenshots\ss2.png')

        textattr = self.driver.find_elements_by_name("abc")
        print("The count of TextBoxes using name attr = ",len(textattr))

        combobox = self.driver.find_elements_by_xpath(".//select")
        print("The count of Combo Box = ",len(combobox))

        radio = self.driver.find_elements_by_class_name("radioclass")
        print("The count of Radio Buttons = ",len(radio))

        linktext = self.driver.find_elements_by_xpath(".//a")
        print("The count of Link Texts = ",len(linktext))

        checkbox = self.driver.find_elements_by_css_selector("input[type='checkbox']")
        print("The count of Check Boxes = ",len(checkbox))

        tag = self.driver.find_elements_by_tag_name("img")
        print("The count of images = ",len(tag))


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
