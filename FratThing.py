from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

def get_email():
    try:
        driver = webdriver.Edge('C:/Users/Aurum/Downloads/MicrosoftWebDriver')
        driver.get("https://www.minuteinbox.com/delete")
        assert "MinuteInbox" in driver.title

    except:
        print('Page Not loaded')
        return -1;

    element_email = driver.find_element_by_id('email')
    email = element_email.text
    driver.close()
    return email

def get_name(email):
    x = email.split('.')
    y = x[1].split('@')
    z = [x[0],y[0]]
    print(z)

    return z

def signup(name,email):
    driver = webdriver.Edge('C:/Users/Aurum/Downloads/MicrosoftWebDriver')
    driver.get("https://www.ownyourprep.com/?ref=phikappataumsu&sba=andrew.butler@kaplan.com")

    element_check = driver.find_element_by_class_name('unchecked')

    element_check.click()

    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(1)
    elements_signup = driver.find_elements_by_class_name("btn signup")
    elements_signup[1].click()


    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID, "input_6_31")))

    driver.find_element_by_id("input_6_31").send_keys(name[1])
    driver.find_element_by_id("input_6_32").send_keys(name[0])
    driver.find_element_by_id("input_6_12").send_keys(email)


    element_drop = driver.find_element_by_id('input_6_20')
    element_drop.click()
    element_drop.send_keys(Keys.ARROW_DOWN)
    element_drop.send_keys(Keys.ENTER)

    element_next = driver.find_element_by_id('gform_submit_button_6')
    element_next.click()

    time.sleep(2)
    driver.close()
    return email

def main():

    x = int(input('How many accounts do you want: '))

    for i in range(0,x):
        email = get_email()
        if email == -1:
            break

        name = get_name(email)
        signup(name,email)


    done = input('Done.... Enter to close.....')

main()
