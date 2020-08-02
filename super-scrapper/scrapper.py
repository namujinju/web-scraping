from bs4 import BeautifulSoup
import requests
# import source


LIMIT = 50


def get_last_page(URL):
    result = requests.get(URL)
    # result = source.html_source()

    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    spans = []
    for link in links[:-1]:
        spans.append(int(link.string))

    max_page = spans[-1]

    return max_page


def extract_job(html):

    title = html.find("h2").find("a")["title"]
    company = html.find("span", "company")
    try:
        if company.find("a") != None:  # 링크가 있음
            company = company.find("a").string
        else:
            company = company.string
        company = company.strip()
    except:
        company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    link = f"https://www.indeed.com/viewjob?jk={job_id}"
    return {"title": title, "company": company, "location": location, "link": link}


def extract_jobs(last_page, URL):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")

        clickcards = soup.find_all(
            "div", {"class": "jobsearch-SerpJobCard"})
        for clickcard in clickcards:
            job = extract_job(clickcard)
            jobs.append(job)

    return jobs


def get_jobs(word):
    URL = f"https://www.indeed.com/jobs?q={word}&limit={LIMIT}"

    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL)
    return jobs
