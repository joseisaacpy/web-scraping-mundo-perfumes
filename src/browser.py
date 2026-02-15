from selenium import webdriver


def init_browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def close_browser(browser):
    browser.quit()
