
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    yield driver
    driver.quit()

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for Amazon is not correct'
    assert "Amazon" in driver.title, 'Title for Amazon is not correct'

    search_homepage = driver.find_element(By.CLASS_NAME, 'a-button-text').click()
    print("\nOpened Amazon Homepage. Title & URL verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver, 5)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_box = driver.find_element(By.ID, 'nav-search-submit-button')
    search_box.click()

    #assert "wireless mouse" in driver.current_url
    assert driver.current_url.__contains__('wireless'),'Search results page did not load'
    assert driver.title.__contains__('wireless'),'Search results page did not load'
    print("\nSearch results page loaded successfully.")
'''
def test_find_element(driver):
    wait = WebDriverWait(driver, 15)

    #Single product title
    first_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,'a h2 span'))
    )
    print("\nFirst Product: ", first_product.text)

    product_titles = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"a h2 span"))
    )
    print(f"\nFound {len(product_titles)} product titles on page one.\n")

    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")

    assert len(product_titles) > 0, "No products found on Amazon search results!"
'''