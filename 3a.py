import numpy as np
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_tag_name("button")
    button.click()
    x = float(browser.find_element_by_id("input_value").text)
    answer = str(np.log(abs(12*np.sin(x))))
    answerInput = browser.find_element_by_id("answer")
    answerInput.send_keys(answer)
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
