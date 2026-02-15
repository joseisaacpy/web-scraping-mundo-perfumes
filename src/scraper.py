from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_link(browser: WebDriver, url: str)-> None:
    browser.get(url)
    
def get_total_pages(browser: WebDriver)-> int:
    pagination_elements = browser.find_elements(By.CLASS_NAME, "MuiPaginationItem-page")
    pages = [int(el.text) for el in pagination_elements if el.text.isdigit()]
    print(f"Foram encontradas {max(pages)} páginas" )
    return max(pages) if pages else 1

def extract_products(browser: WebDriver) -> list[dict]:
    wait = WebDriverWait(browser, 10)
    
    wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='/produto/']"))
    )

    products = []


    cards = browser.find_elements(By.CSS_SELECTOR, "a[href^='/produto/']")


    for card in cards:
        try:
            title = card.find_element(By.CSS_SELECTOR, "p.MuiTypography-body1").text

            prices = card.find_elements(By.CSS_SELECTOR, "p")
            price = None

            for p in prices:
                if "R$" in p.text:
                    price = p.text

            products.append({
                "title": title,
                "price": price
            })

        except Exception:
            continue
    print(f"Foram encontrados {len(products)} produtos")
    return products