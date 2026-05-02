"""
code for working google homepage
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('What browser do you want to use? ')

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case _:
        print('Unknown browser - Not available. \n Executing with default EDGE browser.')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

#       driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage loaded - Pass")
else:
    print("Google Homepage NOT loaded - Fail")

sleep(3)
driver.quit()


