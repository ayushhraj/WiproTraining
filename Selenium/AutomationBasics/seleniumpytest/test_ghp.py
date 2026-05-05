"""
how to test google homepage using pytest and selenium
"""
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google' , 'Google Home Page not loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images','Image Page not loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains('Business'))
    # time.sleep(2)
    # assert 'Business' in driver.title,'Business Page not Loaded - Title Check'
    # assert 'business' in driver.current_url, 'Business Page not Loaded - URL Check'
    check.is_in('Google Business Profile' ,driver.title, 'Business Page not Loaded - Title Check')  #shoft assertion
    check.is_in("business", driver.current_url, "Business Page not Loaded - URL Check")