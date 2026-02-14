from selenium import webdriver


def init_browser():
    browser = webdriver.Chrome()
    return browser

def close_browser(browser):
    browser.quit()