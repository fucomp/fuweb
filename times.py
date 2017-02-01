import selenium as sel
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from html5print import HTMLBeautifier as hbf
import os
import argparse
import names
import time
import random
import string

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

firstname = names.get_first_name()
lastname = names.get_last_name()
email = ''.join([randomword(10), '@', randomword(10), '.com'])
password = randomword(16)

print(' '.join([firstname, lastname, "has decided to sign up for thetimes.co.uk"]))

pwd = os.path.dirname(os.path.realpath(__file__))
path_to_chromedriver = pwd + '/chromedriver'
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
time.sleep(5)
browser.find_element_by_id("firstName").send_keys(firstname)
browser.find_element_by_id("lastName").send_keys(lastname)
browser.find_element_by_id("email").send_keys(email)
browser.find_element_by_id("confirmEmail").send_keys(email)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_id("accountPopSubmit").click()
