from bs4 import BeautifulSoup
import source
import requests


URL = "https://stackoverflow.com/jobs?q=python"
# result = source.html_source()


def get_last_page():
    result = requests.get(URL)
    # result = source.html_source()
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", "s-pagination")
    pages = pagination.find("a")

    return int(pages["title"].split(" ")[-1])


def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    link = f"https://stackoverflow.com/jobs/{job_id}"
    return {"title": title, "company": company, "location": location, "link": link}


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping SO: page: {page}")
        result = requests.get(URL)
        # result = source.html_source()
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", "-job")
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_page()
    return extract_jobs(last_page)
