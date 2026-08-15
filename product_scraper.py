import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
TOTAL_PAGES = 20


def main():
    all_products = []

    for page in range(1, TOTAL_PAGES + 1):
        url = f"{BASE_URL}?page={page}"
        html = fetch_page(url)

        if html is None:
            print(f"Skipping page {page} — could not fetch it.")
            continue

        products = parse_products(html)
        all_products.extend(products)
        print(f"Page {page}: found {len(products)} product(s).")

    if not all_products:
        print("No products found.")
        return

    save_to_csv(all_products, "products.csv")
    print(f"Saved {len(all_products)} product(s) total to products.csv")


def fetch_page(url):
    """Send a GET request to `url` and return the page's HTML as text.
    Returns None if the request was not successful."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_products(html):
    """Parse product listing HTML and return a list of dicts,
    each containing a product's name and price."""
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="product-wrapper")

    products = []
    for card in cards:
        name = card.find("a", class_="title")["title"]
        price = card.find("h4", class_="price float-end card-title pull-right").text.strip()

        product = {"name": name, "price": price}
        products.append(product)

    return products


def save_to_csv(products, filename):
    """Write a list of product dicts to a CSV file with name
    and price columns."""
    with open(filename, "w") as file:
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


if __name__ == "__main__":
    main()