from bs4 import BeautifulSoup
import requests


def export_info(link):
    URL = f"https://comic.naver.com{link}"
    res = requests.get(URL)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    day = link.split("=")[-1]
    title = soup.find("div", "detail").find(
        "h2").get_text().strip().split("\t")[0].strip()
    author = soup.find("span", "wrt_nm").get_text().strip()
    return {"day": day, "title": title, "author": author}


def export_links():

    URL = "https://comic.naver.com/webtoon/weekday.nhn"
    res = requests.get(URL)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    thumb_list = soup.find_all("div", {"class": "thumb"})

    webtoon_link = []

    for thumb in thumb_list:

        webtoon_link.append(thumb.find("a")["href"])
    return webtoon_link


def export_all():
    links = export_links()
    webtoon_info = []
    for i, link in enumerate(links):
        webtoon_info.append(export_info(link))
        print(f"scrapping {i}")

    return webtoon_info
