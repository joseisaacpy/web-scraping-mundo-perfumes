from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def open_link(browser: WebDriver, url: str)-> None:
    browser.get(url)
    
def get_total_pages(browser: WebDriver)-> int:
    pagination_elements = browser.find_elements(By.CLASS_NAME, "MuiPaginationItem-page")
    pages = [int(el.text) for el in pagination_elements if el.text.isdigit()]
    print(f"Foram encontradas {max(pages)} páginas" )
    return max(pages) if pages else 1