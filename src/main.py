from src.browser import init_browser, close_browser
from src.scraper import open_link,get_total_pages,extract_products
from src.storage import save_product_to_csv

BASE_URL = "https://mundo-dos-perfumes-the.stoqui.shop/"
def main():
    browser = init_browser()
    all_products = []
    try:
        open_link(browser, BASE_URL)

        total_pages = get_total_pages(browser)
        for page in range(1, total_pages + 1):
            url = f"{BASE_URL}?page={page}"
            print("Acessando a página:", url)

            open_link(browser, url)
            
            products =extract_products(browser)
            all_products.extend(products)

        save_product_to_csv(all_products)
    finally:
        close_browser(browser)
    
if __name__ == "__main__":
    main()