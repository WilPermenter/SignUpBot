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
    # This will return a list if you dont know, not a string. Add a [0] for that
    z = [x[0], y[0]]

    """
    This could also be condensed to:
    addr = email.split('@')[0]
    name = ' '.join(addr.split('.')) <-- Will Return string from list (with space)

    Basically works like this:
        * Split email at @ ==> ['andrew.butler', 'kaplan.com'][0] ==> 'andrew.butler'
        * Split name at . and iterate over the list, adding each item in a string
          with a ' ' space between them ==> ' '.join(LIST)
    """

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

    """
        Likely should be `driver.find_element_by_name('body')
        https://selenium-python.readthedocs.io/locating-elements.html

        So if I had this element: <div id='cool-div' class='best-div'/>
        I could find it any of these ways:
            * find_element_by_css_selector('div') ==> Only would work for the first element
            * find_element_by_tag_name('cool-div')
            * find_element_by_class_name('best-div')
    """
    driver.find_element_by_tag_name('body').send_keys(Keys.END)

    element_signup = driver.find_element_by_class_name("btn signup")
    """
        Could be wrong about this one, cause ive never used selinium, but looks like they
        have seperate functions for parsing HTML. I believe by doing find_element_* you will only
        recieve the very first element that matches your query. So make sure only one element on the page
        matches what your searching, or use one of the find_elements* methods and search through the list it would
        return you
    """
    print(element_signup.text)
    # Error
    time.sleep(2)

    """
        Need more details on what goes wrong here
    """

    # driver.find_element_by_class_name('signup').click()

    """
        Okay so two things here

        1) Assertions are bad in prod. like I explained on snap. Basically the first
            one of these to assert false with end the program, not keep asserting other stuff
        
        2) Your doing a repetitive task with the only things changing being the data provided,
            a loop could easily condense all of this

            Not 100% on what your trying to do here, but maybe something like this:
            psuedocode, would need to adjust to exactly what ur doing

            page_data = {
                "el_fn": 31,
                "el_ln": 32,
                "el_email": 12,
                "el_drop": 29 
                ...etc ... etc
            }

            for el in page_data.items():
                # el is a tuple ==> ex. ('el_fn', 31)
                data = driver.find_element_by_id(f"input_6_{el[1]}")
                page_data[el[0]] = data
                if "No results found." not in driver.page_source:
                    page_data[el[0]] = None
                
    """
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

""" Normally scripts with one primary func with start like this:

if __name__ == "__main__":
    main()


Basically checks if the name of the module you ran (this one) is the same as the name
of the top scope of code (which is out here, outside any functions and such)
"""
