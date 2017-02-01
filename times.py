import selenium as sel
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from html5print import HTMLBeautifier as hbf
import os
import argparse
import names
import time


firstname = names.get_first_name()
lastname = names.get_last_name()

print(' '.join([firstname, lastname, "has decided to sign up for thetimes.co.uk"]))

pwd = os.path.dirname(os.path.realpath(__file__))

path_to_chromedriver = pwd + '/chromedriver'
print(path_to_chromedriver)

browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = "http://www.thetimes.co.uk/edition/news/rip-off-rail-fares-scrapped-3vdkqtckw"
browser.get(url)

def click_on_element(element_id):
    browser.find_element_by_id(element_id).click()

def retry_for_slow_elements(f, args):
    for i in range(0,5):
        try:
            f(args)
        except ElementNotVisibleException:
            print("Couldn't find element, will retry in 5s")
            time.sleep(5)
            continue
        break

retry_for_slow_elements(click_on_element, "popup-get-access")
