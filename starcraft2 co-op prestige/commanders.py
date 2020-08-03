from bs4 import BeautifulSoup
import requests


def extract_commanders():
    URL = "https://starcraft.fandom.com/wiki/Category:Co-op_Commanders"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    commanders = []
    coms = soup.find_all("li", "category-page__member")

    for com in coms:
        com = com.text.strip().split(" (")[0]
        commanders.append(com)

    commanders = list(map(lambda x: "_".join(x.split(" ")), commanders))
    return commanders
