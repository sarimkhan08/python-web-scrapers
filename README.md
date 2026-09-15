# Python Web Scrapers

A small collection of Python web scrapers built as portfolio projects. Each script fetches a page, parses out structured data with BeautifulSoup, and saves the results to a CSV file.

## Reliability

Both scrapers use a two-stage fetch strategy: a fast plain HTTP request first, and if that returns no usable data (e.g. the page needs JavaScript to render, or blocks simple requests), they automatically fall back to a headless browser via Playwright. This means both scrapers work on static pages as well as JavaScript-heavy or anti-bot-protected ones, without any manual switching.

## Requirements

```
pip install requests beautifulsoup4 playwright
playwright install chromium
```

---

## Job Scraper (`job_scraper.py`)

Scrapes job listings (title, company, location) from [Real Python's fake jobs site](https://realpython.github.io/fake-jobs/), a static site built for scraping practice.

### How it works

1. `fetch_page()` — sends a GET request and returns the page's HTML
2. `parse_jobs()` — uses BeautifulSoup to extract title, company, and location from each job listing
3. If no jobs are found via the request above, `fetch_page_playwright()` automatically retries with a headless browser to fetch the fully rendered page — this handles sites that need JavaScript to load content
4. `save_to_csv()` — writes the results to `jobs.csv`

### Usage

```
python job_scraper.py
```

Output is saved to `jobs.csv` in the same folder, with columns: `title`, `company`, `location`.

### Sample output

```
title,company,location
Senior Python Developer,"Payne, Roberts and Davis","Stewartbury, AA"
Energy engineer,Vasquez-Davidson,"Christopherville, AA"
...
```

---

## Product Scraper (`product_scraper.py`)

Scrapes product name and price data from [Web Scraper's test e-commerce site](https://webscraper.io/test-sites/e-commerce/static/computers/laptops), a paginated practice site.

### How it works

1. `fetch_page()` — sends a GET request and returns the page's HTML
2. Loops through all pages of results, following pagination automatically
3. `parse_products()` — uses BeautifulSoup to extract each product's name and price
4. If a page returns no usable data via the request above, `fetch_page_playwright()` automatically retries with a headless browser to fetch the fully rendered page
5. `save_to_csv()` — writes the combined results from all pages to `products.csv`

### Usage

```
python product_scraper.py
```

Output is saved to `products.csv` in the same folder, with columns: `name`, `price`.

### Sample output

```
name,price
Packard 255 G2,$416.99
Aspire E1-510,$306.99
ThinkPad T540p,$1178.99
...
```
