from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time


def get_email():
    driver = webdriver.Edge('C:/Users/Aurum/Downloads/MicrosoftWebDriver')
    driver.get("https://www.minuteinbox.com/")
    assert "MinuteInbox" in driver.title
    element_email = driver.find_element_by_id('email')
    email = element_email.text
    assert "No results found." not in driver.page_source
    try:
        element_delete = driver.find_element_by_class_name('btn-delete')
        element_delete.click()
    except:
        element_delete = driver.find_element_by_class_name(
            '.gradient .delete-tab')
        element_delete.click()
    else:
        assert "No results found." not in driver.page_source

    driver.close()
    return email


def get_name(email):
    x = email.split('.')
    y = x[1].split('@')
    z = [x[0], y[0]]
    print(z)
    return z


def signup(name, email):
    driver = webdriver.Edge('C:/Users/Aurum/Downloads/MicrosoftWebDriver')
    driver.get(
        "https://www.ownyourprep.com/?ref=phikappataumsu&sba=andrew.butler@kaplan.com")
    assert "Test" in driver.title
    element_check = driver.find_element_by_class_name('unchecked')
    assert "No results found." not in driver.page_source
    element_check.click()

    driver.find_element_by_tag_name('body').send_keys(Keys.END)

    element_signup = driver.find_element_by_class_name("btn signup")
    print(element_signup.text)
    # Error
    time.sleep(2)

    # driver.find_element_by_class_name('signup').click()

    assert "No results found." not in driver.page_source
    element_fn = driver.find_element_by_id('input_6_31')
    assert "No results found." not in driver.page_source
    element_fn.send_keys(name[0])
    element_ln = driver.find_element_by_id('input_6_32')
    assert "No results found." not in driver.page_source
    element_ln.send_keys(name[1])
    element_email = driver.find_element_by_id('input_6_12')
    assert "No results found." not in driver.page_source
    element_email.send_keys(email)

    element_drop = driver.find_element_by_id('input_6_20')
    assert "No resluts found." not in driver.page_source
    element_drop.click()
    element_drop.send_keys(Keys.ARROW_DOWN)

    element_next = driver.find_element_by_class_name('.btn .signup')
    element_next.click()
    assert "No results found." not in driver.page_source
    element_delete = driver.find_element_by_class_name('btn-delete')
    element_delete.click()
    driver.close()
    return email


def main():

    x = int(input('How many accounts do you want: '))

    for i in range(0, x):
        email = get_email()
        name = get_name(email)
        signup(name, email)
    done = input('Done.... Enter to close.....')


main()
