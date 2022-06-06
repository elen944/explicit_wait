from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
    
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),u'100'))
btn = browser.find_element_by_id("book")
btn.click()

import math

def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
    
test=browser.find_element_by_xpath('//*[@id="answer"]')
test.send_keys(calc(x))
    
option3 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
option3.click()
    

time.sleep(30)
browser.quit()