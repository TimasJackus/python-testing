import pytest
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

class TestClass:
    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        first_name = fillAndGetValue(browser, ".first_block .first", "Timas")
        last_name = fillAndGetValue(browser, ".first_block .second", "Jackus")
        email = fillAndGetValue(browser, ".first_block .third", "jackustimas@gmail.com")
        phone_number = fillAndGetValue(browser, ".second_block .first", "+37062730598")
        address = fillAndGetValue(browser, ".second_block .second", "Vilnius, Lithuania")
        button = browser.find_element_by_tag_name("button")
        button.click()
        congratsText = browser.find_element_by_css_selector(".container h1").text
        assert (
            first_name == "Timas" and
            last_name == "Jackus" and
            email == "jackustimas@gmail.com" and
            phone_number == "+37062730598" and
            address == "Vilnius, Lithuania" and
            congratsText == 'Congratulations! You have successfully registered!'
        )

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        first_name = fillAndGetValue(browser, ".first_block .first", "Timas")
        last_name = fillAndGetValue(browser, ".first_block .second", "Jackus")
        email = fillAndGetValue(browser, ".first_block .third", "jackustimas@gmail.com")
        phone_number = fillAndGetValue(browser, ".second_block .first", "+37062730598")
        address = fillAndGetValue(browser, ".second_block .second", "Vilnius, Lithuania")
        button = browser.find_element_by_tag_name("button")
        button.click()
        congratsText = browser.find_element_by_css_selector(".container h1").text
        assert (
            first_name == "Timas" and
            last_name == "Jackus" and
            email == "jackustimas@gmail.com" and
            phone_number == "+37062730598" and
            address == "Vilnius, Lithuania" and
            congratsText == 'Congratulations! You have successfully registered!'
        )
