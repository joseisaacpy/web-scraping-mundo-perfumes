import pandas as pd


def save_product_to_csv(product: list[dict], filename: str="products.csv") -> None:
    df = pd.DataFrame(product)
    df.to_csv(filename, index=False)  
    