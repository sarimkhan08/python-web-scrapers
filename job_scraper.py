import csv
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"


def main():
    html = fetch_page(URL)
    if html is None:
        print("Server is down or the page could not be reached.")
        return

    jobs = parse_jobs(html)
    if jobs == []:
        print("No job listings found.")
        return

    save_to_csv(jobs, "jobs.csv")
    print(f"Saved {len(jobs)} job(s) to jobs.csv")


def fetch_page(url):
    """Send a GET request to `url` and return the page's HTML as text.
    Returns None if the request was not successful."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_jobs(html):
    """Parse job listing HTML and return a list of dicts,
    each containing a job's title, company, and location."""
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="card")

    jobs = []
    for card in cards:
        title = card.find("h2", class_="title is-5").text
        company = card.find("h3", class_="subtitle is-6 company").text
        location = card.find("p", class_="location").text.strip()

        job = {"title": title, "company": company, "location": location}
        jobs.append(job)

    return jobs


def save_to_csv(jobs, filename):
    """Write a list of job dicts to a CSV file with title, company,
    and location columns."""
    with open(filename, "w") as file:
        fieldnames = ["title", "company", "location"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)


if __name__ == "__main__":
    main()