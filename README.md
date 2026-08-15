# Python Web Scrapers

A small collection of Python web scrapers built as portfolio projects. Each script fetches a page, parses out structured data with BeautifulSoup, and saves the results to a CSV file.

## Job Scraper (`job_scraper.py`)

Scrapes job listings (title, company, location) from [Real Python's fake jobs site](https://realpython.github.io/fake-jobs/), a static site built for scraping practice.

### How it works

1. `fetch_page()` — sends a GET request and returns the page's HTML
2. `parse_jobs()` — uses BeautifulSoup to extract title, company, and location from each job listing
3. `save_to_csv()` — writes the results to `jobs.csv`

### Requirements

```bash
pip install requests beautifulsoup4
```

### Usage

```bash
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

*Coming soon — scrapes product name and price data from an e-commerce practice site.*
