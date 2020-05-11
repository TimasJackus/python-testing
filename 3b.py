import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome()

def fillAndGetValue(browser, selector, value):
    try:
        first_name = browser.find_element_by_css_selector(selector)
        first_name.send_keys(value)
        return first_name.get_attribute("value")
    except NoSuchElementException:
        return ""

class TestStringMethods(unittest.TestCase):
    def test_first_form(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        with self.subTest():
            firstName = fillAndGetValue(browser, ".first_block .first", "Timas")
            self.assertEqual(firstName, "Timas")
        with self.subTest():
            last_name = fillAndGetValue(browser, ".first_block .second", "Jackus")
            self.assertEqual(last_name, "Jackus")
        with self.subTest():
            email = fillAndGetValue(browser, ".first_block .third", "jackustimas@gmail.com")
            self.assertEqual(email, "jackustimas@gmail.com")
        with self.subTest():
            phone_number = fillAndGetValue(browser, ".second_block .first", "+37062730598")
            self.assertEqual(phone_number, "+37062730598")
        with self.subTest():
            address = fillAndGetValue(browser, ".second_block .second", "Vilnius, Lithuania")
            self.assertEqual(address, "Vilnius, Lithuania")
        button = browser.find_element_by_tag_name("button")
        button.click()
        with self.subTest():
            congratsText = browser.find_element_by_css_selector(".container h1").text
            self.assertEqual(congratsText, 'Congratulations! You have successfully registered!')


    def test_second_form(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        with self.subTest():
            firstName = fillAndGetValue(browser, ".first_block .first", "Timas")
            self.assertEqual(firstName, "Timas")
        with self.subTest():
            last_name = fillAndGetValue(browser, ".first_block .second", "Jackus")
            self.assertEqual(last_name, "Jackus")
        with self.subTest():
            email = fillAndGetValue(browser, ".first_block .third", "jackustimas@gmail.com")
            self.assertEqual(email, "jackustimas@gmail.com")
        with self.subTest():
            phone_number = fillAndGetValue(browser, ".second_block .first", "+37062730598")
            self.assertEqual(phone_number, "+37062730598")
        with self.subTest():
            address = fillAndGetValue(browser, ".second_block .second", "Vilnius, Lithuania")
            self.assertEqual(address, "Vilnius, Lithuania")
        button = browser.find_element_by_tag_name("button")
        button.click()
        with self.subTest():
            congratsText = browser.find_element_by_css_selector(".container h1").text
            self.assertEqual(congratsText, 'Congratulations! You have successfully registered!')


if __name__ == '__main__':
    unittest.main()
    browser.quit()
