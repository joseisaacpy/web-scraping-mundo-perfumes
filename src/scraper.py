from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def open_link(browser: WebDriver, url: str)-> None:
    browser.get(url)
    
    